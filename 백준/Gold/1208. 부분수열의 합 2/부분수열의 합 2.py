N,S=map(int,input().split())
*l,=map(int,input().split())

left=l[:N//2]
right=l[N//2:]

ls={}
rs={}

for v in range(2**len(left)):
    i=0
    a=0
    while v:
        a+=v%2*left[i]
        v//=2
        i+=1
    ls[a]=ls.get(a,0)+1

for v in range(2**len(right)):
    i=0
    a=0
    while v:
        a+=v%2*right[i]
        v//=2
        i+=1
    rs[a]=rs.get(a,0)+1

ans=-(S==0)

for i in ls:
    ans+=ls[i]*rs.get(S-i,0)

print(ans)