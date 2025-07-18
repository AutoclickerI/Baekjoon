N,*l=[int(i.split()[0])for i in open(0)]
v=[a:=0]*N
for i in l:v[-i]+=1
d=[0]*4**9
for i in v:d[i]+=1
for i in range(4**9):
    if d[i]:
        a+=d[i]-1
        d[i+1]+=d[i]-1
print(a)