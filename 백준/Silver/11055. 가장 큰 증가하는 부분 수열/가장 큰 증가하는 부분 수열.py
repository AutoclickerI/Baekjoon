n=int(input())
a=list(map(int,input().split()))
h=[(1,a[0])]*n
for i in range(1,n):
    try:h[i]=(max([h[j][0] for j in range(i)if a[j]<a[i]])+1,max([h[j][1] for j in range(i)if a[j]<a[i]])+a[i])
    except:h[i]=(1,a[i])
print(max([k[1]for k in h]))   