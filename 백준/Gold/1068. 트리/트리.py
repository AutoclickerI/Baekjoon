def f(x):l[x]=-2;[l[i]==x!=f(i)for i in range(n)]
n,*l,d=map(int,open(0).read().split())
f(d)
print(sum(~l[i]<=0==(i in l)for i in range(n)))