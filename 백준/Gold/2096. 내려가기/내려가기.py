a=[(0,0)]*3
for i in range(int(input())):
    p=list(map(int,input().split()))
    a=[(p[0]+max(a[0][0],a[1][0]),p[0]+min(a[0][1],a[1][1])),(p[1]+max(a[0][0],a[1][0],a[2][0]),p[1]+min(a[0][1],a[1][1],a[2][1])),(p[2]+max(a[2][0],a[1][0]),p[2]+min(a[2][1],a[1][1]))]
print(max(a[0][0],a[1][0],a[2][0]),min(a[0][1],a[1][1],a[2][1]))