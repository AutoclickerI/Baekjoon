import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    N = int(next(it))
    vis = [0] * N  # vis[i] has bit j=1 if i can see j

    for i in range(N):
        row = 0
        for j in range(N):
            if next(it) == b"1":
                row |= 1 << j
        vis[i] = row

    w1 = int(next(it))
    w2 = int(next(it))

    hats = next(it).decode().strip()

    Q = int(next(it))
    queries = []
    for _ in range(Q):
        k = int(next(it))
        asked = [int(next(it)) - 1 for _ in range(k)]
        queries.append(asked)

    # Number of possible hat assignments ("worlds")
    W = 1 << N  # worlds are indexed by an N-bit mask in [0, 2^N)
    all_worlds_mask = (1 << W) - 1  # bitset over worlds; 1 means "world is possible"

    # Precompute masks over world-indices:
    # idx_bit0[p] has 1s at world indices whose p-th bit is 0; idx_bit1[p] similarly.
    idx_bit0 = [0] * N
    idx_bit1 = [0] * N
    for p in range(N):
        half = 1 << p
        step = half << 1
        ones_run = (1 << half) - 1          # 'half' ones
        denom = (1 << step) - 1             # 'step' ones
        repeat_mask = all_worlds_mask // denom  # exact geometric-series replication
        m0 = ones_run * repeat_mask         # blocks: [1...1][0...0] repeated
        idx_bit0[p] = m0
        idx_bit1[p] = all_worlds_mask ^ m0

    # For each player i, Hbits[i] = bits (people) that i cannot see AND are not i.
    all_people_mask = (1 << N) - 1
    Hbits = []
    for i in range(N):
        hidden_other = (all_people_mask ^ (1 << i)) & (~vis[i])
        hb = []
        x = hidden_other
        while x:
            lsb = x & -x
            hb.append(lsb.bit_length() - 1)
            x ^= lsb
        Hbits.append(hb)

    shifts = [1 << p for p in range(N)]  # shift amount in world-index space for flipping bit p

    def saturate_over_hidden(worlds_bitset: int, hb_list: list[int]) -> int:
        """
        OR-saturate 'worlds_bitset' along all world-index dimensions in hb_list:
        within each subcube over those bits, if any world is present, mark all worlds in that subcube present.
        Implemented purely by big-int bit operations.
        """
        b = worlds_bitset
        for p in hb_list:
            sh = shifts[p]
            b |= (b & idx_bit0[p]) << sh
            b |= (b & idx_bit1[p]) >> sh
        return b

    # Build initial possible-worlds set P from the public constraint w1 <= #white <= w2
    if w1 == 0 and w2 == N:
        P = all_worlds_mask
    else:
        arr = bytearray((W + 7) // 8)
        for m in range(W):
            c = m.bit_count()
            if w1 <= c <= w2:
                arr[m >> 3] |= 1 << (m & 7)
        P = int.from_bytes(arr, "little")

    # Real world index from hats string: bit i=1 iff hats[i] == 'W'
    real = 0
    for i, ch in enumerate(hats):
        if ch == "W":
            real |= 1 << i

    out_lines = []
    for asked in queries:
        oldP = P
        newP = oldP
        ans_chars = []

        for i in asked:
            # Saturate oldP over bits i cannot see (excluding i).
            satP = saturate_over_hidden(oldP, Hbits[i])

            # Existence of candidates for (obs, i=0) and (obs, i=1), kept in separate i-slices
            E0 = satP & idx_bit0[i]  # worlds with i-bit=0 that exist in some hidden-variation class
            E1 = satP & idx_bit1[i]  # worlds with i-bit=1 ...

            shi = shifts[i]

            # Replicate each slice across the i dimension so existence depends only on observation (not i itself)
            E0_any = E0 | (E0 << shi)
            E1_any = E1 | (E1 >> shi)

            # In a world, player i knows their color iff exactly one of {i=0 candidate, i=1 candidate} exists.
            Yset = oldP & (E0_any ^ E1_any)   # worlds where i would answer 'Y'
            # Since every world in oldP must allow at least its own i-bit, answer is always Y or N inside oldP:
            Nset = oldP & ~Yset               # worlds where i would answer 'N'

            isY = (Yset >> real) & 1
            if isY:
                ans_chars.append("Y")
                newP &= Yset
            else:
                ans_chars.append("N")
                newP &= Nset

        out_lines.append("".join(ans_chars))
        P = newP  # apply the public update for the next query

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()