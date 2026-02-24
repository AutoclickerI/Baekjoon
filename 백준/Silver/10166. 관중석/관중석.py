D1,D2=map(int,input().split())
ss=set()
for i in range(D1,D2+1):
    for j in range(i):
        ss.add(j*pow(i,-1,10**9+7)%(10**9+7))
print(len(ss))