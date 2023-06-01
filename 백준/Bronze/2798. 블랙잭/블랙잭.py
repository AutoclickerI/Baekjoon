a = list(map(int, input().split()))
a[0] -= 2
b = list(map(int, input().split()))
c = 0
for i in range(a[0]):
    for j in range(a[0]-i):
        for k in range(a[0]-i-j):
            n = b[i] + b[i + j + 1] + b[i + j + k + 2]
            if n <= a[1]:
                if n > c:
                    c = n
print(c)