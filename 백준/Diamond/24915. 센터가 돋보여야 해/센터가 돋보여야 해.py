import sys

def ints():
    data = sys.stdin.buffer.read()
    n = len(data)
    i = 0
    while i < n:
        while i < n and data[i] <= 32:
            i += 1
        if i >= n:
            break
        sign = 1
        if data[i] == 45:  # '-'
            sign = -1
            i += 1
        x = 0
        while i < n and data[i] > 32:
            x = x * 10 + (data[i] - 48)
            i += 1
        yield sign * x

it = ints()
N = next(it); Q = next(it)

NEG = -10**30
POS =  10**30

# node as (mx, mn, AB, BC, ABC)
def merge(L, R):
    Lmx, Lmn, LAB, LBC, LABC = L
    Rmx, Rmn, RAB, RBC, RABC = R

    mx = Lmx if Lmx > Rmx else Rmx
    mn = Lmn if Lmn < Rmn else Rmn

    AB = LAB
    t = RAB
    if t > AB: AB = t
    t = Rmx - Lmn
    if t > AB: AB = t

    BC = LBC
    t = RBC
    if t > BC: BC = t
    t = Lmx - Rmn
    if t > BC: BC = t

    ABC = LABC
    t = RABC
    if t > ABC: ABC = t
    t = LAB - Rmn
    if t > ABC: ABC = t
    t = RBC - Lmn
    if t > ABC: ABC = t

    return (mx, mn, AB, BC, ABC)

tree = [(NEG, POS, NEG, NEG, NEG)] * (2 * N)

# build leaves
for i in range(N):
    v = next(it)
    tree[i + N] = (v, v, NEG, NEG, NEG)

# build internal
for i in range(N - 1, 0, -1):
    tree[i] = merge(tree[i << 1], tree[i << 1 | 1])

neutral = (NEG, POS, NEG, NEG, NEG)
out_lines = []
append_out = out_lines.append
merge_local = merge
tree_local = tree
N_local = N

def update(idx, val):
    i = idx + N_local
    tree_local[i] = (val, val, NEG, NEG, NEG)
    i >>= 1
    while i:
        tree_local[i] = merge_local(tree_local[i << 1], tree_local[i << 1 | 1])
        i >>= 1

def query(l, r):  # [l, r)
    l += N_local
    r += N_local
    left = neutral
    right = neutral
    while l < r:
        if l & 1:
            left = merge_local(left, tree_local[l])
            l += 1
        if r & 1:
            r -= 1
            right = merge_local(tree_local[r], right)
        l >>= 1
        r >>= 1
    return merge_local(left, right)[4]

for _ in range(Q):
    typ = next(it); a = next(it); b = next(it)
    if typ == 1:
        update(a - 1, b)
    else:
        append_out(str(query(a - 1, b)) + "\n")

sys.stdout.write("".join(out_lines))