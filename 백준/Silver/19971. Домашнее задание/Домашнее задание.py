f=lambda:[*map(int,input().split())]
n,m=f()
t=f()
b={f()[0]for _ in[0]*m}
a=0
for i in range(n):a=max(a,t[i]*(-~i not in b))
print(sum(t)-a)