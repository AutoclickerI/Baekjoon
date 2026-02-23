import sys
from array import array

BASE = 10**9
CHUNK = 9

# ---------- fast parsing: read bytes once, parse tokens without split() ----------
def parse_input_numbers():
    data = sys.stdin.buffer.read()
    n_data = len(data)
    i = 0

    # skip spaces
    while i < n_data and data[i] <= 32:
        i += 1

    # parse n
    n = 0
    while i < n_data and data[i] > 32:
        n = n * 10 + (data[i] - 48)
        i += 1

    pool = array('i')     # all chunks for all numbers (LS chunk first)
    offs = array('I')     # offset into pool
    lens = array('I')     # number of chunks
    sgns = array('b')     # +1 / -1

    for _ in range(n):
        while i < n_data and data[i] <= 32:
            i += 1

        sign = 1
        if i < n_data and data[i] == 45:  # '-'
            sign = -1
            i += 1

        start = i
        while i < n_data and data[i] > 32:
            i += 1
        end = i

        off = len(pool)

        p = end
        # parse from end in <=9-digit chunks; slice length <= 9 => tiny copy
        while p > start:
            q = p - CHUNK
            if q < start:
                q = start
            pool.append(int(data[q:p]))
            p = q

        ln = len(pool) - off
        if ln == 0:
            pool.append(0)
            ln = 1

        offs.append(off)
        lens.append(ln)
        sgns.append(sign)

    return n, pool, offs, lens, sgns

# ---------- Kadane accumulator (lazy chunk add), uses >= BASE exactly ----------
def acc_getsign(di, sign):
    return sign * (-1 if di[-1] < 0 else 1)

def acc_trim(di):
    while len(di) > 1 and di[-1] == 0:
        di.pop()

def acc_add_pool(di, sign, pool, off, ln, other_sign):
    # ensure length
    cur_len = len(di)
    if cur_len < ln:
        di.extend(array('i', [0]) * (ln - cur_len))

    s_mul = sign * other_sign
    L = len(di)
    for idx in range(L):
        f = 1
        if idx < ln:
            di[idx] += pool[off + idx] * s_mul
            f = 0

        if di[idx] <= -BASE:
            f = 0
            di[idx] += BASE
            if idx == L - 1:
                di.append(-1)
                L += 1
            else:
                di[idx + 1] -= 1

        if di[idx] >= BASE:  # stick to >= BASE
            f = 0
            di[idx] -= BASE
            if idx == L - 1:
                di.append(1)
                L += 1
            else:
                di[idx + 1] += 1

        if f:
            break

    acc_trim(di)

# ---------- normalize a segment sum (like your B_decimal.normalize), >= BASE ----------
def normalize_sum(acc_q):
    # acc_q: array('q') possibly with negative entries
    sign = 1

    while len(acc_q) > 1 and acc_q[-1] == 0:
        acc_q.pop()

    if acc_q[-1] < 0:
        sign = -1
        for i in range(len(acc_q)):
            acc_q[i] = -acc_q[i]

    i = 0
    while i < len(acc_q):
        x = acc_q[i]
        if x < 0:
            up = -(x // BASE)              # 0 - (x//BASE)
            acc_q[i] = x + BASE * up
            if i == len(acc_q) - 1:
                acc_q.append(0)
            acc_q[i + 1] -= up

        x = acc_q[i]
        if x >= BASE:  # stick to >= BASE
            up = x // BASE
            acc_q[i] = x - BASE * up
            if i == len(acc_q) - 1:
                acc_q.append(0)
            acc_q[i + 1] += up

        i += 1

    # match your: while 1<len and di[-1] < 1: pop
    while len(acc_q) > 1 and acc_q[-1] < 1:
        acc_q.pop()

    if len(acc_q) == 1 and acc_q[0] == 0:
        sign = 1

    # digits now nonnegative < BASE
    di = array('I', acc_q)
    return sign, di

# ---------- compare big numbers (sign, array('I') digits LS-first) ----------
def big_greater(a_sign, a_di, b_sign, b_di):
    if a_sign != b_sign:
        return a_sign > b_sign
    la, lb = len(a_di), len(b_di)
    if la != lb:
        if a_sign > 0:
            return la > lb
        else:
            return la < lb
    # same length
    k = la - 1
    while k >= 0:
        av = a_di[k]
        bv = b_di[k]
        if av != bv:
            if a_sign > 0:
                return av > bv
            else:
                return av < bv
        k -= 1
    return False

def big_to_str(sign, di):
    if len(di) == 1 and di[0] == 0:
        return "0"
    parts = [str(di[-1])]
    for x in reversed(di[:-1]):
        parts.append(f"{x:09d}")
    return ("-" if sign < 0 else "") + "".join(parts)

# ---------- main ----------
def main():
    n, pool, offs, lens, sgns = parse_input_numbers()

    # forward boundaries
    cur_di = array('i', [0])
    cur_sign = 1
    fbd = array('I', [0])

    for i in range(n):
        if acc_getsign(cur_di, cur_sign) > 0:
            acc_add_pool(cur_di, cur_sign, pool, offs[i], lens[i], sgns[i])
        else:
            # reset: copy digits from pool
            off = offs[i]
            ln = lens[i]
            cur_di = pool[off:off + ln]  # array('i') slice copy
            cur_sign = sgns[i]
            fbd.append(i)

    fbd.append(n)

    # backward boundaries (compute on reversed, then map like your code)
    cur_di = array('i', [0])
    cur_sign = 1
    bskip = array('I', [0])

    for ri in range(n):
        idx = n - 1 - ri
        if acc_getsign(cur_di, cur_sign) > 0:
            acc_add_pool(cur_di, cur_sign, pool, offs[idx], lens[idx], sgns[idx])
        else:
            off = offs[idx]
            ln = lens[idx]
            cur_di = pool[off:off + ln]
            cur_sign = sgns[idx]
            bskip.append(ri)

    # map to original indices
    bbd = array('I')
    for x in bskip:
        bbd.append(n - x)
    bbd.append(0)
    bbd = array('I', reversed(bbd))  # now ascending boundaries

    # intersect and evaluate segments on the fly
    best_sign = 1
    best_di = array('I', [0])
    has_best = False

    i = 0
    j = 0
    while i + 1 < len(fbd) and j + 1 < len(bbd):
        fS, fE = fbd[i], fbd[i + 1]
        bS, bE = bbd[j], bbd[j + 1]
        S = fS if fS > bS else bS
        E = fE if fE < bE else bE

        if S < E:
            # find maxLen (first pass)
            maxLen = 1
            for k in range(S, E):
                lk = lens[k]
                if lk > maxLen:
                    maxLen = lk

            acc = array('q', [0]) * maxLen

            # accumulate digits (second pass)
            for k in range(S, E):
                off = offs[k]
                ln = lens[k]
                s = sgns[k]
                if s == 1:
                    for t in range(ln):
                        acc[t] += pool[off + t]
                else:
                    for t in range(ln):
                        acc[t] -= pool[off + t]

            sgn, di = normalize_sum(acc)

            if (not has_best) or big_greater(sgn, di, best_sign, best_di):
                best_sign, best_di = sgn, di
                has_best = True

        if fE < bE:
            i += 1
        else:
            j += 1

    # fallback: max single element (safety)
    if not has_best:
        for k in range(n):
            ln = lens[k]
            off = offs[k]
            s = sgns[k]
            # build as normalized sum of a single number
            acc = array('q', [0]) * ln
            if s == 1:
                for t in range(ln):
                    acc[t] = pool[off + t]
            else:
                for t in range(ln):
                    acc[t] = -pool[off + t]
            sgn, di = normalize_sum(acc)
            if (not has_best) or big_greater(sgn, di, best_sign, best_di):
                best_sign, best_di = sgn, di
                has_best = True

    sys.stdout.write(big_to_str(best_sign, best_di) + "\n")

if __name__ == "__main__":
    main()