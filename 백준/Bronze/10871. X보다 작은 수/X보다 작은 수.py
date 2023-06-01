n = int(input().split(' ')[1])
a = input().split(' ')
ans = []
for i in range(len(a)):
    if int(a[i]) < n:
        ans.append(a[i])
pnt = ans[0]
for i in range(1, len(ans)):
    pnt += f' {ans[i]}'
print(pnt)