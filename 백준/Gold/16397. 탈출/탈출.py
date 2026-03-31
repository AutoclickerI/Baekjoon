N,T,G=map(int,input().split())

v=[float('inf')]*100000

v[N]=0

l=[(0,N)]

for c,n in l:
    if n+1<100000 and c+1<v[n+1]:
        v[n+1]=c+1
        l+=(c+1,n+1),
    if 0<n<50000 and c+1<v[n*2-10**(len(str(n*2))-1)]:
        v[n*2-10**(len(str(n*2))-1)]=c+1
        l+=(c+1,n*2-10**(len(str(n*2))-1)),

r=v[G]
print('ANG'*(T<r)or r)