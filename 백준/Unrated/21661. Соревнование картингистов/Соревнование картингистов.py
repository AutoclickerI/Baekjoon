f=lambda:map(int,input().split())
n,_=f()
x=[]
l=[]
for _ in range(n):x+=input(),;l+=sum(f()),
m=min(l)
print(x[max(i*(l[i]==m)for i in range(n))])