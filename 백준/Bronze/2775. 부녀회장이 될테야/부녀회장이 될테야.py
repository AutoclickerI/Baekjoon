a = [list(range(1, 15))]
for i in range(1, 15):
    a.append([1])
    for j in range(1, 14):
        a[i].append(a[i][j - 1] + a[i - 1][j])
for i in range(int(input())):
    print(a[int(input())][int(input()) - 1])