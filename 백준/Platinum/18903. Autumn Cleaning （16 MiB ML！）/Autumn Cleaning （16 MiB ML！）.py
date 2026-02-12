import sys

def pack(P, k):
    ba = bytearray()
    for v in P:
        ba.extend(int(v).to_bytes(k, 'little'))
    return int.from_bytes(ba, 'little')

def poly_mul(A, B):
    if [] in [A, B]:
        return []
    if min(min(A), min(B)) < 0:
        raise ValueError("Not implemented with negative integer.")
    maxA = max(A)
    maxB = max(B)
    bl = max(1, 0 - max(maxA, maxB, maxA * maxB * min(len(A), len(B))).bit_length() // -8)

    a = pack(A, bl)
    b = pack(B, bl)
    c = a * b
    c = c.to_bytes((len(A) + len(B) - 1) * bl, 'little')

    return [int.from_bytes(c[i*bl:(i+1)*bl], 'little') for i in range(len(A) + len(B) - 1)]


MOD = 1000003

def fast_ints():
    data = sys.stdin.buffer.read()
    n = len(data)
    i = 0
    while i < n:
        while i < n and data[i] <= 32:
            i += 1
        if i >= n:
            return
        x = 0
        while i < n and data[i] > 32:
            x = x * 10 + (data[i] - 48)
            i += 1
        yield x

def norm(P):
    while P and P[-1] == 0:
        P.pop()
    return P

def add_poly(acc, poly, k):
    if not poly:
        return acc
    if not acc:
        # poly is already truncated+reduced
        return poly[:]  # copy
    L = len(poly)
    if len(acc) < L:
        acc.extend([0] * (L - len(acc)))
    # coefficients kept < MOD, so one subtraction is enough each add
    for i in range(L):
        v = acc[i] + poly[i]
        if v >= MOD:
            v -= MOD
        acc[i] = v
    if len(acc) > k + 1:
        del acc[k+1:]
    return norm(acc)

def solve():
    it = fast_ints()
    n = next(it)
    k = next(it)
    r = next(it)

    if k > n:
        print(0)
        return

    cnt = [0] * r
    for _ in range(n):
        a = next(it)
        cnt[a % r] += 1

    # inv[i] for i=1..k (k <= 3000)
    inv = [0] * (k + 1)
    for i in range(1, k + 1):
        inv[i] = pow(i, MOD - 2, MOD)

    # F[t] is polynomial in y for residue t
    F = [[1]] + [[] for _ in range(r - 1)]

    for x in range(r):
        c = cnt[x]
        if c == 0:
            continue

        d = min(c, k)

        # Build H_s(y) polynomials: H[s][i] = C(c,i) if (x*i)%r==s else 0
        H = [[0] * (d + 1) for _ in range(r)]
        C = 1  # C(c,0)
        for i in range(d + 1):
            H[(x * i) % r][i] = C
            if i < d:
                # C(c,i+1) = C(c,i) * (c-i) / (i+1)
                C = (C * (c - i)) % MOD
                C = (C * inv[i + 1]) % MOD

        # Normalize H to avoid useless multiplications
        nonempty_s = []
        for s in range(r):
            norm(H[s])
            if H[s]:
                nonempty_s.append(s)

        newF = [[] for _ in range(r)]
        for t in range(r):
            Ft = F[t]
            if not Ft:
                continue
            for s in nonempty_s:
                Hs = H[s]
                # Convolution in degree
                prod = poly_mul(Ft, Hs)
                if len(prod) > k + 1:
                    prod = prod[:k + 1]
                prod = [v % MOD for v in prod]
                norm(prod)
                u = (t + s) % r
                newF[u] = add_poly(newF[u], prod, k)

        F = newF

    ans_poly = F[0]
    ans = ans_poly[k] if len(ans_poly) > k else 0
    print(ans % MOD)

if __name__ == "__main__":
    solve()
