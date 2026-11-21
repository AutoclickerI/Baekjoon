def f(c):L,O,V,E=map((c+x).count,'LOVE');return(L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)%100*-1,c
x,_,*s=open(0)
print(min(s,key=f))