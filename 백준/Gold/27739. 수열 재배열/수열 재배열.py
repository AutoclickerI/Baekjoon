N,K=map(int,input().split())
*l,=map(int,input().split())
increasing=[]
for i in range(N):
    tmp=0
    c=i
    while c<N and l[c]>tmp:
        tmp=l[c]
        c+=1
    increasing+=c-i,
decreasing=[]
for i in range(N)[::-1]:
    tmp=2001
    c=i
    while -1<c and l[c]<tmp:
        tmp=l[c]
        c-=1
    decreasing+=i-c,
decreasing=decreasing[::-1]
m=K
for i in range(N-K+1):
    if 0<=i-1 and l[i-1]<min(l[i:i+K]) and i+K<N and l[i+K]>max(l[i:i+K]):
        m=max(m,K+decreasing[i-1]+increasing[i+K])
    else:
        if 0<=i-1:
            m=max(m,decreasing[i-1]+sum(j>l[i-1]for j in l[i:i+K]))
        if i+K<N:
            m=max(m,increasing[i+K]+sum(j<l[i+K]for j in l[i:i+K]))
print(m)