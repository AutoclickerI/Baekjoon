n,m,t,a,*l=map(int,open(0).read().split())
print(max(a-m,0)+sum(i-min(a+2*m,a:=i)for i in l)+max(t-a-m,0))