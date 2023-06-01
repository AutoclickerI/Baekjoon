p,q=map(int,input().split())
l=[0,*map(int,input().split())]
for i in range(p):l[i+1]+=l[i]
a=s=e=0
while p-e+1:
    t=l[e]-l[s]
    a+=t==q
    if t>q:s+=1
    else:e+=1
print(a)