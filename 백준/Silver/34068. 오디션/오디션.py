N,*l=[int(i.split()[0])for i in open(0)]
v=[a:=0]*N
for i in l:v[-i]+=1
d=[0]*6**7
for i in v:d[i]+=1
for i in range(4**9):f=max(d[i]-1,0);a+=f;d[i+1]+=f
print(a)