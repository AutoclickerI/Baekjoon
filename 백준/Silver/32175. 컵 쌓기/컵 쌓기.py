N,H=map(int,input().split())
d={}
for i in map(int,input().split()):d[i]=d.get(i,0)+1
l=[0,1]
for i in range(H):
    l+=0,
    for j in d:
        l[-1]+=d[j]*l[max(0,2+i-j)]
    l[-1]%=10**9+7
print(l[-1])