i,*l=map(str.split,open(0))
x=1
k=int(i[1])
for f,s in l:
 f=int(f)
 if'C'<s:x=max(x,f)
 else:k=min(k,f)
print(x+1,k-1)