x=y=w=0
p,q=open(0)
for i,j in zip(p.split(),q.split()):
 if i>j:x+=3;w=1
 elif i<j:y+=3;w=2
 else:x+=1;y+=1
print(x,y,'DAB'[w]*(x==y)or'AB'[x<y])