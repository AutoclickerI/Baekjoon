m=[0]*99
a=10
for i in[*open(0,'rb')][1:]:
 v=1
 for c in i[-2::-1]:m[c]-=v;v*=10
print(-sum(i*(a:=a-1)for i in sorted(m)))