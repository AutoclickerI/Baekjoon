F,S,G,U,D=map(int,input().split())
v={}
s,*q='use the stairs',(S,0)
for i,c in q:
 for n in i+U,i-D:q+=[(n,c+1)]*(0<n<=v.get(n,F));v[n]=0
 if i==G:s=c
print(s)