N,*l=open(0)
N=int(N)
i=0
while'*'not in l[i]:i+=1
v=l[i].index('*')
i+=1
h=i+1,v+1
la,ra=v-l[i].find('*'),l[i].rfind('*')-v
i+=1
x=0
while l[i+x].count('*')<2:x+=1
*l,=zip(*l[i+x:])
print(*h)
print(la,ra,x,*filter(int,[i.count('*')for i in l]))