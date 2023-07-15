N,K=map(int,input().split())
*l,=map(int,input().split())
*l1,=(l[i]-K*i for i in range(N))
*l2,=(l[-i-1]-K*i for i in range(N))
m1=l1[0]
M1=l1[1]-l1[0]
for i in l1[1:]:
    M1=max(i-m1,M1)
    m1=min(i,m1)
m2=l2[0]
M2=l2[1]-l2[0]
for i in l2[1:]:
    M2=max(i-m2,M2)
    m2=min(i,m2)
print(max(M1,M2))