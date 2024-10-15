r=range
def f():n,m=map(int,input().split());return n,m,[input()for i in r(n)]
for T in r(int(input())):n,m,l=f();x,y,z=f();print(sum(l==[a[j:j+m]for a in z[i:i+n]]for i in r(x)for j in r(y)))