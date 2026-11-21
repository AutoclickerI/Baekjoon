class node:
    def __init__(self,t):
        m,f,_=t
        self.min_mid=m
        self.max_mid=m
        self.min_fin=f
        self.max_fin=f
        self.num=1
    def cross(self,t):
        m,f,_=t
        return m<=self.max_mid or f<=self.max_fin
    def add(self,t):
        m,f,_=t
        self.min_mid=min(self.min_mid,m)
        self.max_mid=max(self.max_mid,m)
        self.min_fin=min(self.min_fin,f)
        self.max_fin=max(self.max_fin,f)
        self.num+=1
    def merge(self,newnode):
        self.min_mid=min(self.min_mid,newnode.min_mid)
        self.max_mid=max(self.max_mid,newnode.max_mid)
        self.min_fin=min(self.min_fin,newnode.min_fin)
        self.max_fin=max(self.max_fin,newnode.max_fin)
        self.num+=newnode.num
    def __repr__(self):
        return f'node object(mid: [{self.min_mid}, {self.max_mid}], fin: [{self.min_fin}, {self.max_fin}], num: {self.num})'

N=int(input())
students_midsort=sorted((*map(int,input().split()),i)for i in range(N))
students_finalsort=sorted(students_midsort,key=lambda s:s[1])
used=[0]*N
use_count=0

nodes=[]
idx_mid=0
idx_fin=0
flag=False
while use_count<N:
    
    while idx_mid<N:
        if used[students_midsort[idx_mid][2]]:
            idx_mid+=1
        else:
            break
    else:
        break
    
    if not flag:
        nodes+=node(students_midsort[idx_mid]),
        used[students_midsort[idx_mid][2]]=1
        idx_mid+=1
        use_count+=1
        
    flag=False
    
    while idx_mid<N:
        if used[students_midsort[idx_mid][2]]:
            idx_mid+=1
            continue
        if nodes[-1].cross(students_midsort[idx_mid]):
            used[students_midsort[idx_mid][2]]=1
            flag=True
            nodes[-1].add(students_midsort[idx_mid])
            idx_mid+=1
            use_count+=1
        else:
            break
    
    while idx_fin<N:
        if used[students_finalsort[idx_fin][2]]:
            idx_fin+=1
            continue
        if nodes[-1].cross(students_finalsort[idx_fin]):
            used[students_finalsort[idx_fin][2]]=1
            flag=True
            nodes[-1].add(students_finalsort[idx_fin])
            idx_fin+=1
            use_count+=1
        else:
            break        
    
splitter=[i.num for i in nodes]
def getval(p,q,r):
    return max(p,q,r)-min(p,q,r)
if len(splitter)<3:
    print(-1)
else:
    s,m,*splitter=splitter
    e=sum(splitter)
    ans=getval(s,m,e)
    mli=[m]
    eli=splitter
    i=j=k=0
    while k<len(eli):
        mli+=eli[k],
        m+=eli[k]
        e-=eli[k]
        k+=1
        ans=min(ans,getval(s,m,e))
        while s<m and j<len(mli):
            s+=mli[j]
            m-=mli[j]
            j+=1
            ans=min(ans,getval(s,m,e))
        for _ in[0]*2:
            if j:
                j-=1
                s-=mli[j]
                m+=mli[j]
    print(ans)