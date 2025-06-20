SAFE=1
BROKEN=0
(_,k),*l=[[*map(eval,i.split())]for i in open(0)]
x=1
for f,s in l:
 if s:x=max(x,f)
 else:k=min(k,f)
print(x+1,k-1)