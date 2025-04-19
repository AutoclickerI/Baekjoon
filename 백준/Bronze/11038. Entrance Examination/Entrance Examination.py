import sys
input = sys.stdin.readline

def solve():
    while True:
        m, nmin, nmax = map(int, input().split())
        if m == 0 and nmin == 0 and nmax == 0:
            break

        # Read m scores, already in descending order
        P = [int(input()) for _ in range(m)]

        best_gap = -1
        best_n   = nmin

        # Try each possible number of successful applicants
        for n in range(nmin, nmax + 1):
            gap = P[n-1] - P[n]   # P[n-1] is nth score, P[n] is (n+1)th score
            # Update if gap is larger, or same but n is larger
            if gap > best_gap or (gap == best_gap and n > best_n):
                best_gap = gap
                best_n   = n

        print(best_n)

if __name__ == "__main__":
    solve()
