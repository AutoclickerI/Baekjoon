N=int(input())
s=1
v=1
print(N*2-1)
for i in range(N-1):
    print(s,s+N-1,v,1)
    s+=N
    v+=1
    print(s,s,N,v)
    s+=1
print(N*N,N*N,N,1)