import sys
import math

def compute_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

def main():
    def solve():
        n_and_rest = open(0).read().split()
        n = int(n_and_rest[0])
        b = list(map(int, n_and_rest[1:n+1]))
        n_minus_1 = n - 1

        n = len(b)
        divisors = compute_divisors(n)

        valid_gcds = set()
        for g in divisors:
            S = [0]*g
            for i in range(n):
                S[i % g] += b[i]
            if all(s == 0 for s in S):
                valid_gcds.add(g)

        output = []
        for x in range(1, n):
            g = math.gcd(x, n)
            if g in valid_gcds:
                output.append('1')
            else:
                output.append('0')
        print(' '.join(output))

    solve()

if __name__ == "__main__":
    main()