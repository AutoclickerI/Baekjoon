def count_suspicious(events):
    logged_in = set()
    suspicious = 0
    for a in events:
        if a > 0:
            logged_in.add(a)
        else:
            x = -a
            if x not in logged_in:
                suspicious += 1
            else:
                logged_in.remove(x)
    return suspicious

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    events = list(map(int, input().split()))
    print(count_suspicious(events))
