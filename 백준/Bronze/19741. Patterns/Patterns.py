def solve():
    import sys
    input = sys.stdin.readline
    n, k = map(int, input().split())
    
    # Precompute number of divisors for numbers from 1 to n^2.
    max_val = n * n
    divisors = [0] * (max_val + 1)
    
    for num in range(1, max_val + 1):
        # Count divisors by iterating up to sqrt(num)
        count = 0
        d = 1
        while d * d <= num:
            if num % d == 0:
                count += 1
                if d * d != num:
                    count += 1
            d += 1
        divisors[num] = count

    # Build and output the picture
    output_lines = []
    for i in range(n):
        line_chars = []
        for j in range(n):
            num = i * n + j + 1
            if divisors[num] <= k:
                line_chars.append('*')
            else:
                line_chars.append('.')
        output_lines.append("".join(line_chars))
    
    sys.stdout.write("\n".join(output_lines))
    
if __name__ == '__main__':
    solve()
