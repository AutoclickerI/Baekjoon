import sys

def ints_from_stdin():
    data = sys.stdin.buffer.read()
    n = len(data)
    i = 0
    while i < n:
        # skip whitespace
        while i < n and data[i] <= 32:
            i += 1
        if i >= n:
            return
        sign = 1
        if data[i] == 45:  # b'-'
            sign = -1
            i += 1
        j = i
        while i < n and data[i] > 32:
            i += 1
        # bytes slice total across all tokens is bounded by input size (<= ~10MB)
        yield sign * int(data[j:i])

it = ints_from_stdin()
N = next(it)

# Non-empty max subarray
a1 = next(it)
base = a1
off = 0  # cur = base - off

best_base = base
best_off = 0
best_val = a1        # cached value of best (may become stale if best_off updates under same base)
best_dirty = False
best_bitlen = best_val.bit_length() if best_val > 0 else 0

for _ in range(N - 1):
    x = next(it)

    # Kadane step using (base, off): cur > 0 <=> base > off
    if base > off:
        off -= x
    else:
        base = x
        off = 0

    # Update best, trying hard to avoid materializing huge integers
    if base == best_base:
        # base equal => compare base - off vs base - best_off  <=>  off < best_off
        if off < best_off:
            best_off = off
            best_dirty = True
        continue

    # Need best_val if bases differ (lazy recompute)
    if best_dirty:
        best_val = best_base - best_off
        best_dirty = False
        best_bitlen = best_val.bit_length() if best_val > 0 else 0

    # Safe skip: if off >= 0 then cur <= base, so base <= best_val => cannot beat best
    if off >= 0 and base <= best_val:
        continue

    # Optional safe skip when best is positive and cur is provably much smaller by bit length
    # cur = base + (-off) when off < 0, and |cur| < 2^(max(bitlen(base), bitlen(-off)) + 1)
    if off < 0 and best_val > 0:
        t = -off
        mb = base.bit_length()
        tb = t.bit_length()
        m = mb if mb > tb else tb
        # If m <= best_bitlen - 3, then cur < 2^(m+1) <= 2^(best_bitlen-2) < 2^(best_bitlen-1) <= best_val
        if m <= best_bitlen - 3:
            continue

    cur_val = base - off  # materialize only when necessary
    if cur_val > best_val:
        best_base = base
        best_off = off
        best_val = cur_val
        best_dirty = False
        best_bitlen = best_val.bit_length() if best_val > 0 else 0

# Finalize (if best moved under same base without refreshing best_val)
if best_dirty:
    best_val = best_base - best_off

print(best_val)