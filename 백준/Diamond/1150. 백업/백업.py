from heapq import*

N,K,*arr=map(int,open(0).read().split())

*lix,=range(-1,N-1)
*rix,=range(1,N+1)
rv=[j-i for i,j in zip(arr,arr[1:])]
lv=[0]+rv
rv+=0,

hq=[]
for i in range(N-1):
    heappush(hq,(arr[i+1]-arr[i],i,i+1))

r=0
cnt=0
v=[0]*N
while cnt<K:
    if not hq:
        break
    l,s,e=heappop(hq)
    if v[s] or v[e]:
        continue

    v[s]=v[e]=1

    r+=l
    cnt+=1

    if 0<=lix[s] and rix[e]<N:
        t=lv[s]+rv[e]-l
        heappush(hq,(t,lix[s],rix[e]))
        lv[rix[e]]=t
        rv[lix[s]]=t

        lix[rix[e]]=lix[s]
        rix[lix[s]]=rix[e]

print(r)