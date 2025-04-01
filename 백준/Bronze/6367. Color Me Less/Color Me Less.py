def solve():
    import sys
    input = sys.stdin.readline
    
    # Read the 16 target colors.
    targets = []
    for _ in range(16):
        r, g, b = map(int, input().split())
        targets.append((r, g, b))
    
    results = []
    while True:
        line = input().strip()
        if not line:
            break
        r, g, b = map(int, line.split())
        # Check termination condition.
        if r == -1 and g == -1 and b == -1:
            break
        
        # Initialize best match.
        best_color = None
        best_distance = None
        
        # Find the target color with the smallest squared Euclidean distance.
        for tr, tg, tb in targets:
            dr = r - tr
            dg = g - tg
            db = b - tb
            distance = dr * dr + dg * dg + db * db  # Squared distance
            if best_distance is None or distance < best_distance:
                best_distance = distance
                best_color = (tr, tg, tb)
        
        # Format the result.
        results.append(f"({r},{g},{b}) maps to ({best_color[0]},{best_color[1]},{best_color[2]})")
    
    sys.stdout.write("\n".join(results))
    
if __name__ == '__main__':
    solve()
