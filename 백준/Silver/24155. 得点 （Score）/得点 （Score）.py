n,*l=open(0)
s=sorted(l,key=int)[::-1]
for i in l:print(s.index(i)+1)