import sys

data = sys.stdin.buffer.read().split()
it = iter(map(int, data))

N = next(it); Q = next(it)
NEG = -10**30
POS =  10**30

# 5 parallel arrays for segment tree
mx  = [NEG] * (2 * N)
mn  = [POS] * (2 * N)
AB  = [NEG] * (2 * N)
BC  = [NEG] * (2 * N)
ABC = [NEG] * (2 * N)

# leaves
base = N
for idx in range(N):
    v = next(it)
    p = base + idx
    mx[p] = v
    mn[p] = v

# build
for p in range(N - 1, 0, -1):
    l = p << 1
    r = l | 1

    Lmx = mx[l]; Rmx = mx[r]
    Lmn = mn[l]; Rmn = mn[r]

    mxp = Lmx if Lmx > Rmx else Rmx
    mnp = Lmn if Lmn < Rmn else Rmn

    # AB = max(L.AB, R.AB, R.max - L.min)
    abp = AB[l]
    t = AB[r]
    if t > abp: abp = t
    t = Rmx - Lmn
    if t > abp: abp = t

    # BC = max(L.BC, R.BC, L.max - R.min)
    bcp = BC[l]
    t = BC[r]
    if t > bcp: bcp = t
    t = Lmx - Rmn
    if t > bcp: bcp = t

    # ABC = max(L.ABC, R.ABC, L.AB - R.min, R.BC - L.min)
    abcp = ABC[l]
    t = ABC[r]
    if t > abcp: abcp = t
    t = AB[l] - Rmn
    if t > abcp: abcp = t
    t = BC[r] - Lmn
    if t > abcp: abcp = t

    mx[p] = mxp; mn[p] = mnp
    AB[p] = abp; BC[p] = bcp; ABC[p] = abcp

out = []
append_out = out.append

def update(idx, val):
    p = idx + base
    mx[p] = val
    mn[p] = val
    AB[p] = BC[p] = ABC[p] = NEG
    p >>= 1
    while p:
        l = p << 1
        r = l | 1

        Lmx = mx[l]; Rmx = mx[r]
        Lmn = mn[l]; Rmn = mn[r]

        mxp = Lmx if Lmx > Rmx else Rmx
        mnp = Lmn if Lmn < Rmn else Rmn

        abp = AB[l]
        t = AB[r]
        if t > abp: abp = t
        t = Rmx - Lmn
        if t > abp: abp = t

        bcp = BC[l]
        t = BC[r]
        if t > bcp: bcp = t
        t = Lmx - Rmn
        if t > bcp: bcp = t

        abcp = ABC[l]
        t = ABC[r]
        if t > abcp: abcp = t
        t = AB[l] - Rmn
        if t > abcp: abcp = t
        t = BC[r] - Lmn
        if t > abcp: abcp = t

        mx[p] = mxp; mn[p] = mnp
        AB[p] = abp; BC[p] = bcp; ABC[p] = abcp

        p >>= 1

def query(l, r):  # [l, r)
    l += base
    r += base

    # left accumulator
    lmx = NEG; lmn = POS; lab = NEG; lbc = NEG; labc = NEG
    # right accumulator
    rmx = NEG; rmn = POS; rab = NEG; rbc = NEG; rabc = NEG

    while l < r:
        if l & 1:
            # left = merge(left, node[l])
            Lmx, Lmn, LAB, LBC, LABC = lmx, lmn, lab, lbc, labc
            Rmx, Rmn, RAB, RBC, RABC = mx[l], mn[l], AB[l], BC[l], ABC[l]

            nmx = Lmx if Lmx > Rmx else Rmx
            nmn = Lmn if Lmn < Rmn else Rmn

            nab = LAB
            t = RAB
            if t > nab: nab = t
            t = Rmx - Lmn
            if t > nab: nab = t

            nbc = LBC
            t = RBC
            if t > nbc: nbc = t
            t = Lmx - Rmn
            if t > nbc: nbc = t

            nabc = LABC
            t = RABC
            if t > nabc: nabc = t
            t = LAB - Rmn
            if t > nabc: nabc = t
            t = RBC - Lmn
            if t > nabc: nabc = t

            lmx, lmn, lab, lbc, labc = nmx, nmn, nab, nbc, nabc
            l += 1

        if r & 1:
            r -= 1
            # right = merge(node[r], right)
            Lmx, Lmn, LAB, LBC, LABC = mx[r], mn[r], AB[r], BC[r], ABC[r]
            Rmx, Rmn, RAB, RBC, RABC = rmx, rmn, rab, rbc, rabc

            nmx = Lmx if Lmx > Rmx else Rmx
            nmn = Lmn if Lmn < Rmn else Rmn

            nab = LAB
            t = RAB
            if t > nab: nab = t
            t = Rmx - Lmn
            if t > nab: nab = t

            nbc = LBC
            t = RBC
            if t > nbc: nbc = t
            t = Lmx - Rmn
            if t > nbc: nbc = t

            nabc = LABC
            t = RABC
            if t > nabc: nabc = t
            t = LAB - Rmn
            if t > nabc: nabc = t
            t = RBC - Lmn
            if t > nabc: nabc = t

            rmx, rmn, rab, rbc, rabc = nmx, nmn, nab, nbc, nabc

        l >>= 1
        r >>= 1

    # merge(left, right) and return ABC
    Lmx, Lmn, LAB, LBC, LABC = lmx, lmn, lab, lbc, labc
    Rmx, Rmn, RAB, RBC, RABC = rmx, rmn, rab, rbc, rabc

    abcp = LABC
    t = RABC
    if t > abcp: abcp = t
    t = LAB - Rmn
    if t > abcp: abcp = t
    t = RBC - Lmn
    if t > abcp: abcp = t
    return abcp

for _ in range(Q):
    typ = next(it); a = next(it); b = next(it)
    if typ == 1:
        update(a - 1, b)
    else:
        append_out(str(query(a - 1, b)) + "\n")

sys.stdout.write("".join(out))