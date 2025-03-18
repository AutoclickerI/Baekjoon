def solve():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return

    n = int(data[0].strip())
    heroes = list(map(int, data[1].split()))
    villains = list(map(int, data[2].split()))
    
    # Define a function that returns True if heroes win given d training days.
    def wins(d):
        for h, v in zip(heroes, villains):
            if h + d > v:
                return True
            elif h + d < v:
                return False
        return True  # if all pairs are equal, heroes win by default.
    
    # Binary search for the minimum d such that wins(d) is True.
    lo = 0
    hi = max((v - h for h, v in zip(heroes, villains)), default=0) + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if wins(mid):
            hi = mid
        else:
            lo = mid + 1
    
    sys.stdout.write(str(lo))
    
if __name__ == "__main__":
    solve()
