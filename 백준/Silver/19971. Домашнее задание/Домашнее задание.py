f=lambda:[*map(int,input().split())]
n,m=f()
t=f()
b={f()[0]for _ in[0]*m}
print(sum(t)+min(t[i]*~-(-~i in b)for i in range(n)))