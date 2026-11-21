def solve():
    import sys
    input_data = sys.stdin.read().splitlines()
    n = int(input_data[0])
    results = []
    
    for i in range(1, n+1):
        street = input_data[i]
        length = len(street)
        banned = [False] * length
        
        for j in range(length):
            if street[j] == 'D':
                banned[j] = True
            elif street[j] == 'B':
                banned[j] = True
                if j-1 >= 0:
                    banned[j-1] = True
                if j-2 >= 0:
                    banned[j-2] = True
            elif street[j] == 'S':
                banned[j] = True
                if j-1 >= 0:
                    banned[j-1] = True
                if j+1 < length:
                    banned[j+1] = True

        count = 0
        for j in range(length):
            if street[j] == '-' and not banned[j]:
                count += 1
        results.append(str(count))
    
    sys.stdout.write(" ".join(results))

if __name__ == '__main__':
    solve()
