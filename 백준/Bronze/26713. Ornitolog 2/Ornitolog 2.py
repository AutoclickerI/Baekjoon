n,*l=map(int,open(0).read().split())
z=l[:]
c=v=0
for i in range(1,n):f=l[i-1];f=[0,f<=l[i],f>=l[i]][p:=i%-2|1];F=z[i-1];F=[0,F>=z[i],F<=z[i]][p];p*=1e9;l[i]-=f*p;c+=f;z[i]+=F*p;v+=F
print(min(c,v))