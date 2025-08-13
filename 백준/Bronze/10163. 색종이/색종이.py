d=[-1]*6**8
for i in[*open(c:=0)][1:]:p,q,r,s=map(int,i.split());z=0;exec('v=p+z<<10|q;d[v:v+s]=[c]*s;z+=1;'*r);c+=1
print(*map(d.count,range(c)))