def solve():
    import sys
    data = sys.stdin.read().splitlines()
    T = int(data[0].strip())
    case = 1
    results = []
    
    for i in range(1, 2 * T, 2):
        # Read starting position and command string.
        start_x, start_y = map(int, data[i].split())
        commands = data[i + 1].strip()
        
        # Initial state: position and direction (0=north, 1=east, 2=south, 3=west)
        current_x, current_y = start_x, start_y
        direction = 0  # facing north initially
        visited = {(current_x, current_y): 1}
        
        for cmd in commands:
            if cmd == 'R':
                direction = (direction + 1) % 4
            elif cmd == 'L':
                direction = (direction - 1) % 4
            elif cmd == 'F':
                if direction == 0:       # North
                    current_y += 1
                elif direction == 1:     # East
                    current_x += 1
                elif direction == 2:     # South
                    current_y -= 1
                elif direction == 3:     # West
                    current_x -= 1
                # Record visit
                visited[(current_x, current_y)] = visited.get((current_x, current_y), 0) + 1
        
        # Count locations visited more than once.
        revisits = sum(1 for count in visited.values() if count > 1)
        results.append(f"Case #{case}: {current_x} {current_y} {revisits}")
        case += 1

    sys.stdout.write("\n".join(results))
    
if __name__ == "__main__":
    solve()
