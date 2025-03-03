class shape:
    def __init__(self,data=[]):
        self.data=data
    def __str__(self):
        return ':'.join(''.join(i)for i in self.data)or'None'
    def __repr__(self):
        return f'shape({str(self.data)})'
reg=[shape()for _ in[0]*101]

N,M=map(int,input().split())
for i in range(N):
    reg[i+1]=shape([[*input()]])
for _ in[0]*M:
    o,i,j,k=input().split()
    if o=='1':
        data=reg[int(i)].data
        reg[int(j)]=shape([['-']*4+i[4:] for i in data if ['-']*4+i[4:]!=['-']*8])
        reg[int(k)]=shape([i[:4]+['-']*4 for i in data if i[:4]+['-']*4!=['-']*8])
    if o=='2':
        reg[int(j)]=shape([(i*2)[8-2*int(k):16-2*int(k)]for i in reg[int(i)].data])
    if o=='3':
        if 'None'in(str(reg[int(i)]),str(reg[int(j)])):
            reg[int(k)]=shape()
            continue
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
    
print(reg[100])