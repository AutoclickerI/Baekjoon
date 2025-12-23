def pool(arr):
    if len(arr)<2:
        return arr[0][0]
    N=len(arr)
    return sorted([pool([i[:N//2]for i in arr[:N//2]]),pool([i[:N//2]for i in arr[N//2:]]),pool([i[N//2:]for i in arr[:N//2]]),pool([i[N//2:]for i in arr[N//2:]])])[2]

print(pool([[*map(int,i.split())]for i in open(0)][1:]))  