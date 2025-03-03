class shape:
    def __init__(self,data=[]):
        self.data=data
    def __str__(self):
        return ':'.join(''.join(i)for i in self.data)or'None'
    def __repr__(self):
        return f'shape({str(self.data)})'

def move(*l):
    o,i,j,k=map(str,l)
    if o=='1':
        data=reg[int(i)].data
        reg[int(j)]=shape([['-']*4+i[4:] for i in data if ['-']*4+i[4:]!=['-']*8])
        reg[int(k)]=shape([i[:4]+['-']*4 for i in data if i[:4]+['-']*4!=['-']*8])
    if o=='2':
        reg[int(j)]=shape([(i*2)[8-2*int(k):16-2*int(k)]for i in reg[int(i)].data])
    if o=='3':
        if 'None'in(str(reg[int(i)]),str(reg[int(j)])):
            reg[int(k)]=shape()
            return
        data=[v[:]for v in reg[int(i)].data]+[['-']*8 for _ in[0]*8]
        idx=4
        flag=1
        while 0<=idx and flag:
            idx-=1
            for p,q in zip(data[idx:],reg[int(j)].data):
                for r,s in zip(p,q):
                    flag&='-'in(r,s)
        idx+=1
        for p,q in zip(data[idx:],reg[int(j)].data):
            p[:]=[max(r,s)for r,s in zip(p,q)]
        while data[-1]==['-']*8:data.pop()
        reg[int(k)]=shape(data[:4])
    if o=='4':
        data=[v[:]for v in reg[int(i)].data]
        for p in data:
            for q in range(4):
                if p[q*2]!='-':p[q*2+1]=k
        reg[int(j)]=shape(data)

reg=[shape()for _ in[0]*101]

possible=[0]*8
N=int(input())
for i in range(N):
    s=input()
    reg[i+1]=shape([[*s]])
    for i,j in zip(*[iter(s)]*2):
        if i=='-':continue
        if j=='u':
            possible['SWRC'.find(i)*2]=1
        possible['SWRC'.find(i)*2+1]=1

a=input().split(':')

check=[0]*8
for s in a:
    for i,j in zip(*[iter(s)]*2):
        if i=='-':continue
        if j=='u':
            check['SWRC'.find(i)*2]=1
        check['SWRC'.find(i)*2+1]=1

flag=1
for i,j in zip(possible,check):
    if j:
        flag&=i

if flag:
    ans=[]
    def push(o,i,j,k):
        ans.append((o,i,j,k))
        move(o,i,j,k)
        
    for i in range(1,N+1):
        push(1,i,12,11)
        push(2,11,11,3)
        push(2,12,12,1)
        push(1,11,13,11)
        push(1,12,14,12)
        push(2,13,13,1)
        push(2,14,14,1)
        for i in range(11,15):
            if reg[i].data:
                p,q=reg[i].data[0][:2]
                if p=='-':continue
                v='SWRC'.find(p)
                if q=='u'and str(reg[92+v*2])=='None':
                    push(1,i,15,92+v*2)
                if str(reg[92+v*2+1])=='None':
                    push(1,i,15,92+v*2+1)

    ztr=9
    for i in a:
        f=1
        for j in range(4):
            p,q=i[2*j],i[2*j+1]
            if p=='-':
                continue
            v='SWRC'.find(p)
            if q=='u':
                if j==0:
                    push(2,92+v*2,90+f+ztr*f,1)
                    push(2,90+f+ztr*f,90+f+ztr*f,3)
                else:
                    push(2,92+v*2,90+f+ztr*f,j)
            else:
                push(4,92+v*2+1,92+v*2+1,q)
                if j==0:
                    push(2,92+v*2+1,90+f+ztr*f,1)
                    push(2,90+f+ztr*f,90+f+ztr*f,3)
                else:
                    push(2,92+v*2+1,90+f+ztr*f,j)
            
            if f:
                f=0
            else:
                push(3,91+ztr,90,91+ztr)
            
        if ztr:
            ztr=0
        else:
            push(3,100,91,100)
            
    print(len(ans))
    for i in ans:print(*i)
     
else:
    print(-1)