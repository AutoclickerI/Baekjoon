N=int(input())
t=0
c=1
while t+c<N:
    t+=c
    c+=1
N-=t
print(c-N+1,N)