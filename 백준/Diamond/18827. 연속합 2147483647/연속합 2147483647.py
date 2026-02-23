chunk_length=5
chunk_size=10**chunk_length

class B_decimal:
    def __init__(self,di,sign=1):
        self.di=di
        self.sign=sign
    def __iadd__(self,n):
        if len(self.di)<len(n.di):
            self,n=n,self
        for i in range(len(self.di)):
            f=1
            if i<len(n.di):
                self.di[i]+=n.di[i]*self.sign*n.sign
                f=0
            if self.di[i]<=-chunk_size:
                f=0
                self.di[i]+=chunk_size
                if i==len(self.di)-1:
                    self.di+=-1,
                else:
                    self.di[i+1]-=1
            if chunk_size<=self.di[i]:
                f=0
                self.di[i]-=chunk_size
                if i==len(self.di)-1:
                    self.di+=1,
                else:
                    self.di[i+1]+=1
            if f:
                break
        while 1<len(self.di)and self.di[-1]==0:
            self.di.pop()
        return self
    def normalize(self):
        if self.di[-1]<0:
            self.sign*=-1
            for i in range(len(self.di)):
                self.di[i]*=-1
        i=0
        while i<len(self.di):
            if self.di[i]<0:
                up=0-self.di[i]//chunk_size
                self.di[i]+=chunk_size*up
                if i==len(self.di)-1:
                    self.di+=0,
                self.di[i+1]-=up
            if 9<self.di[i]:
                up=self.di[i]//chunk_size
                self.di[i]-=chunk_size*up
                if i==len(self.di)-1:
                    self.di+=0,
                self.di[i+1]+=up
            i+=1
        while 1<len(self.di)and self.di[-1]<1:
            self.di.pop()
    def getsign(self):
        return self.sign*(-(self.di[-1]<0)|1)
    def __str__(self):
        return'-'*(self.sign<1)+''.join(str(i).zfill(chunk_length)for i in self.di[::-1])

def to_chunked_list(s):
    i=0
    ret=[]
    while i<len(s):
        ret+=int(s[i:i+chunk_length][::-1]),
        i+=chunk_length
    return ret

def to_B_decimal(s):
    if s[0]=='-':
        return B_decimal(to_chunked_list(s[1:][::-1]),-1)
    return B_decimal(to_chunked_list(s[::-1]))

s=[*open(0)][1].split()

*l,=map(to_B_decimal,s)
n=to_B_decimal('0')
forward_skip=[0]
for i in range(len(l)):
    if 0<n.getsign():
        n+=l[i]
    else:
        n=l[i]
        forward_skip+=i,
forward_skip+=len(l),
forward_pass=[(i,j)for i,j in zip(forward_skip,forward_skip[1:])]

*l,=map(to_B_decimal,s[::-1])
n=to_B_decimal('0')
backward_skip=[0]
for i in range(len(l)):
    if 0<n.getsign():
        n+=l[i]
    else:
        n=l[i]
        backward_skip+=i,
backward_skip=([len(l)-i for i in backward_skip]+[0])[::-1]
backward_pass=[(i,j)for i,j in zip(backward_skip,backward_skip[1:])]

arr=[]
i=0
j=0
while i<len(forward_pass)and j<len(backward_pass):
    fS,fE=forward_pass[i]
    bS,bE=backward_pass[j]
    ss=max(fS,bS)
    ee=min(fE,bE)
    if ss<ee:arr+=(ss,ee),
    if fE<bE:
        i+=1
    else:
        j+=1

*l,=map(to_B_decimal,s)
v=[]

for s,e in arr:
    if s==e:continue
    r=sorted([l[i]for i in range(s,e)],key=lambda i:len(i.di))[::-1]
    arr=[0]*len(r[0].di)
    for i in range(len(arr)):
        j=0
        while j<len(r):
            if i==len(r[j].di):
                r.pop()
            else:
                arr[i]+=r[j].di[i]*r[j].sign
                j+=1
    n=B_decimal(arr)
    n.normalize()
    v+=int(str(n)),
print(max(v))