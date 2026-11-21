input()
l=input().split()
d={}
flag=0
for idx,i in enumerate(l):
    d[i]=d.get(i,0)+1
    if d[i]==5:
        flag=1
        
if flag:
    ans=len(l)
    ad=[{}]
    ptr_s=0
    for idx,i in enumerate(l):
        tmp={**ad[-1]}
        tmp[i]=tmp.get(i,0)+1
        while tmp[i]-ad[ptr_s].get(i,0)>4:
            ans=min(ans,idx-ptr_s+1)
            ptr_s+=1
        ad+=tmp,
    print(ans)
else:
    print(-1)