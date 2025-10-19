*l,=map(int,[*open(0)][1].split())
d={}
for i in l:d[i]=d.get(i,0)+1
s=[]
a=[]
for i in l[::-1]:
    while s and d[s[-1]]<=d[i]:
        s.pop()
    if s:
        a+=s[-1],
    else:
        a+=-1,
    s+=i,
print(*a[::-1])