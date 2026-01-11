[K,N],*l=[[*map(int,i.split())][::-1]for i in open(0)]
l.sort()
m=v=i=0
for x,g in l:
 v+=g
 while 2*K<x-l[i][0]:v-=l[i][1];i+=1
 m=max(m,v)
print(m)