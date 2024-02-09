x=y=w=0
for i,j in zip(l:=open(0).read().split(),l[10:]):
 if i>j:x+=3;w=1
 elif i<j:y+=3;w=2
 else:x+=1;y+=1
s="DAB"[w]+"AB";print(x,y,s[(x>y)-(x<y)])