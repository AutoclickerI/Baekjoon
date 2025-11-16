K,L,*l=open(0).read().split()
s=set()
v=[]
for i in l[::-1]:
    if i not in s:
        s.add(i)
        v+=i,
print(*v[::-1][:int(K)])