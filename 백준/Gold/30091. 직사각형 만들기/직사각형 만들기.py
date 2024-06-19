n=int(input())
l=sorted(map(int,input().split()))
d={}
m=0
for i in range(n):
    for j in range(i+1,n):
        d[l[i]+l[j]]=d.get(l[i]+l[j],0)+l[i]*l[j]
        m=max(m,d[l[i]+l[j]])
print(m)