*l,=[[*map(int,i.split())]for i in open(0)]
s=[]
r=0
for i in l:
    if 1<len(i):
        s+=i,
    if s:
        s[-1][-1]-=1
        if s[-1][-1]<1:
            r+=s.pop()[1]
print(r)