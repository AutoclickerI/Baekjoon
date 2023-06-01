l=[]
for i in[0]*9:l+=[*map(int,input().split())]
print(m:=max(l))
p=l.index(m)
print(p//9+1,p%9+1)