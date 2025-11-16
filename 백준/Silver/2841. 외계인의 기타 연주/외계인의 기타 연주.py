_,*l=[map(int,i.split())for i in open(0)]
v=[[c:=0]for _ in[0]*7]
for n,x in l:
 while x<v[n][-1]:c+=1;v[n].pop()
 if v[n][-1]-x:v[n]+=x,;c+=1
print(c)