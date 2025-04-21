T = int(input())

for case_num in range(1, T + 1):
    n, P, Q = map(int, input().split())
    eggs = list(map(int, input().split()))
    eggs.sort()
    
    count = 0
    total_weight = 0

    for weight in eggs:
        if count < P and total_weight + weight <= Q:
            count += 1
            total_weight += weight
        else:
            break

    print(f"Case {case_num}: {count}")
