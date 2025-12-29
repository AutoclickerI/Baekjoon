[N],*l=[[*map(int,i.split())]for i in open(0)]
l.sort()
p=[0]
s=[0]
v=[]
for x,a in l:
    v+=x,
    p+=p[-1]+a,
    s+=s[-1]+a*x,

m=float('inf')
for i in range(N):
    nm=s[-1]-s[i+1]-s[i]-v[i]*(p[-1]-p[i+1]-p[i])
    if nm<m:
        m=nm
        r=i
print(v[r])