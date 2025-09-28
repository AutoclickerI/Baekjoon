def f(x):l[x]=-2;[l[i]==x!=f(i)for i in R]
n,*l,d=map(int,open(0).read().split())
R=range(n)
f(d)
print(sum(~l[i]<1>(i in l)for i in R))