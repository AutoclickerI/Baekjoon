def solve():
    import sys, math
    input_data = sys.stdin.read().strip().splitlines()
    out_lines = []
    for line in input_data:
        # read 4 integers from the line
        parts = line.split()
        if len(parts) != 4:
            continue
        nums = list(map(int, parts))
        if nums == [-1, -1, -1, -1]:
            break
        
        A = nums[:]  # the 4 numbers
        missing = None
        missing_idx = -1
        for i in range(4):
            if A[i] == -1:
                missing = -1
                missing_idx = i
                break

        candidate_arith = None
        candidate_geo = None

        # Try arithmetic candidate:
        if missing_idx == 0:
            # Sequence: [?, a, b, c]
            a, b, c = A[1], A[2], A[3]
            if (b - a) == (c - b):
                d = b - a
                candidate_arith = a - d
        elif missing_idx == 1:
            # Sequence: [a, ?, b, c]
            a, b, c = A[0], A[2], A[3]
            if (c - a) % 3 == 0:
                d = (c - a) // 3
                if a + 2*d == b:
                    candidate_arith = a + d
        elif missing_idx == 2:
            # Sequence: [a, b, ?, c]
            a, b, c = A[0], A[1], A[3]
            if (c - a) % 3 == 0:
                d = (c - a) // 3
                if a + d == b:
                    candidate_arith = a + 2*d
        elif missing_idx == 3:
            # Sequence: [a, b, c, ?]
            a, b, c = A[0], A[1], A[2]
            if (b - a) == (c - b):
                d = b - a
                candidate_arith = c + d

        # Try geometric candidate:
        if missing_idx == 0:
            # Sequence: [?, a, b, c]
            a, b, c = A[1], A[2], A[3]
            if a != 0 and b % a == 0:
                r = b // a
                # Check if a, b, c form a geometric sequence with ratio r
                if a * r == b and b * r == c:
                    if r != 0 and a % r == 0:
                        candidate_geo = a // r
        elif missing_idx == 1:
            # Sequence: [a, ?, b, c]
            a, b, c = A[0], A[2], A[3]
            if a != 0:
                # We need b == a*r^2 and c == a*r^3.
                if b % a == 0 and c % a == 0:
                    r2 = b // a
                    r3 = c // a
                    # Try to deduce r from r2. r must be integer with r*r == r2.
                    r = int(round(math.sqrt(r2)))
                    if r * r == r2 and a * (r**3) == c:
                        candidate_geo = a * r
        elif missing_idx == 2:
            # Sequence: [a, b, ?, c]
            a, b, c = A[0], A[1], A[3]
            if a != 0 and b % a == 0:
                r = b // a
                if a * (r**3) == c:
                    candidate_geo = a * (r**2)
        elif missing_idx == 3:
            # Sequence: [a, b, c, ?]
            a, b, c = A[0], A[1], A[2]
            if a != 0 and b % a == 0:
                r = b // a
                if a * (r**2) == c:
                    candidate_geo = a * (r**3)

        candidate = None
        # Prefer one candidate if it is valid (in range 1..10000)
        if candidate_arith is not None and 1 <= candidate_arith <= 10000:
            candidate = candidate_arith
        if candidate_geo is not None and 1 <= candidate_geo <= 10000:
            if candidate is None:
                candidate = candidate_geo
            else:
                # In a valid input the two methods (if both work) should yield the same candidate.
                if candidate != candidate_geo:
                    candidate = candidate_arith  # arbitrarily choose arithmetic candidate

        if candidate is None:
            candidate = -1

        out_lines.append(str(candidate))
    sys.stdout.write("\n".join(out_lines))
    
if __name__ == '__main__':
    solve()
