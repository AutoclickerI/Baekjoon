n,t=open(0)
n=int(n)
k=t.index('x')
for p in range(10):
    t=t[:k]+chr(p+ord('0'))+t[k+1:]
    s=0
    for i in range(n-1):
        u=int(t[i])*[2,1][i+n&1]
        s+=u//10+u%10
    if s*9%10 == int(t[-2]):print(p);break