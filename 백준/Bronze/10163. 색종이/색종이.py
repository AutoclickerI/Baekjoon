d=[-1]*6**8
for i in[*open(c:=0)][1:]:
 p,q,r,s=map(int,i.split())
 for i in range(r*s):d[(p+i//s)*1002+q+i%s]=c
 c+=1
print(*map(d.count,range(c)))