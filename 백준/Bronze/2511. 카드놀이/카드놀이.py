f=lambda:input().split()
x=y=w=0
for i,j in zip(f(),f()):x+=1+2*(i>j)-(i<j);y+=1+2*(i<j)-(i>j);w=-~(i<j)*(i!=j)or w
s='DAB'[w]+'AB';print(x,y,s[(x>y)-(x<y)])