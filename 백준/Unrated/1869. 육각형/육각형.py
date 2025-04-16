N=int(input())
*l,=map(int,input().split())
d={}

for i in l:
    d[i]=d.get(i,0)+1

l=[]

compress={}

for idx,i in enumerate(sorted(d)):
    compress[i]=idx
    l+=[i]*min(d[i],4)

ans=0
N=len(l)
v=set()

Nd=len(d)

def to_1d(a,b,c,d):
    return ((a*Nd+b)*Nd+c)*Nd+d

for i in range(N):
    d[l[i]]-=1
    for j in range(i+1,N):
        d[l[j]]-=1
        for k in range(j+1,N):
            d[l[k]]-=1
            for m in range(i+1,N):
                if m in(i,j,k):
                    continue
                d[l[m]]-=1
                vs=to_1d(compress[l[i]],compress[l[j]],compress[l[k]],compress[l[m]])
                if vs not in v:
                    sub=l[m]-l[i]
                    if l[j]==l[k]:
                        ans+=d.get(l[j]+sub,0)>1
                    else:
                        ans+=d.get(l[j]+sub,0)*d.get(l[k]+sub,0)>0
                    v.add(vs)
                d[l[m]]+=1
            d[l[k]]+=1
        d[l[j]]+=1
    d[l[i]]+=1

print(ans)