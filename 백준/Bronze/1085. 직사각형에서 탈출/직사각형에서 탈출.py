b = list(map(int, input().split()))
a = [b[0], b[1], b[2]-b[0], b[3]-b[1]]
a.sort()
print(a[0])