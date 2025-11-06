N,M,*l=map(int,open(0).read().split())
l.sort()

v=[]
while l and 0<l[-1]:v+=l.pop(),

l+=[0]*(M-len(l)%M)
v+=[0]*(M-len(v)%M)

a=0
ma=0
for i in zip(*[iter(l+v)]*M):
    a+=abs(i[0])
    ma=max(ma,abs(i[0]))
print(a*2-ma)