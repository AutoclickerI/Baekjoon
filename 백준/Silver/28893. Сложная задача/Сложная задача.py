input()
l1=input().split()
input()
l2=input().split()

v1=c1=l1.count('1')
v=[0]*(len(l1)-c1)
idx=0
for i in l1:
    if i=='0':
        v[idx]=c1
        idx+=1
    else:
        c1-=1

m=-1
idx=0
v2=c2=l2.count('1')
for i in l2:
    if idx==len(v):
        break
    if i=='0':
        m=max(m,idx+min(c2,v[idx]))
        idx+=1
    else:
        c2-=1
print(max(m+1,min(v1,v2)))