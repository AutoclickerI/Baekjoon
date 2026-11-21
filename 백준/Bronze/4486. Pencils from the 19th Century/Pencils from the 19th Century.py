def solve():
    import sys
    data = sys.stdin.read().splitlines()
    case = 1
    results = []
    
    for line in data:
        if not line.strip():
            continue
        N = int(line.strip())
        if N == 0:
            break
        
        # Prepare output for this case
        output = []
        output.append(f"Case {case}:")
        output.append(f"{N} pencils for {N} cents")
        
        found = False
        # Iterate x (four-cent pencils) starting from 1
        # Use a reasonable upper bound: since y = 3N - 15x must be >= 1, x <= (3N - 1)/15.
        for x in range(1, (3 * N - 1) // 15 + 1):
            y = 3 * N - 15 * x
            z = 14 * x - 2 * N
            if y < 1 or z < 1:
                continue
            found = True
            output.append(f"{x} at four cents each")
            output.append(f"{y} at two for a penny")
            output.append(f"{z} at four for a penny")
            output.append("")  # blank line after each solution
        
        if not found:
            output.append("No solution found.")
            output.append("")  # blank line
        
        results.append("\n".join(output))
        case += 1
    
    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    solve()
