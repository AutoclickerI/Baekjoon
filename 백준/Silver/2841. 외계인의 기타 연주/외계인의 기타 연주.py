[N,P],*l=[map(int,i.split())for i in open(0)]
v=[[]for _ in[0]*-~N]
c=0
for n,x in l:
    while v[n]and x<v[n][-1]:
        c+=1
        v[n].pop()
    if v[n]and v[n][-1]==x:c-=1;v[n].pop() 
    v[n]+=x,
    c+=1
print(c)