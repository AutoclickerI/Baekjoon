ptr=0

def getindent(s):
    i=0
    while s[i]==' ':i+=1
    return i

def matmul(a,b):
    return[[sum(b[k][j]*i[k]for k in range(len(i)))%10000 for j in range(len(b[0]))]for i in a]

def matpow(a,k):
    if k==1:
        return a
    t=matpow(a,k//2)
    t=matmul(t,t)
    if k%2:
        t=matmul(t,a)
    return t

class execblock:
    def __init__(self):
        self.multblock=[[[i==j for i in range(27)]for j in range(27)]]
        self.printblock=[]
    def ismultblock(self):
        return self.printblock==[]

s=[*open(0)]
def parse(arr):
    global ptr
    indent=getindent(arr[ptr])
    block=execblock()
    while indent==getindent(arr[ptr]):
        c,*l=arr[ptr].split()
        if c=='REPEAT':
            ptr+=1
            subblock=parse(arr)
            if subblock.ismultblock():
                block.multblock[-1]=matmul(block.multblock[-1],matpow(subblock.multblock[0],int(l[0])))
            else:
                for _ in[0]*int(l[0]):
                    block.multblock[-1]=matmul(block.multblock[-1],subblock.multblock[0])
                    block.multblock+=subblock.multblock[1:]
                    block.printblock+=subblock.printblock
        elif c=='PRINT':
            block.printblock+=l
            block.multblock+=[[i==j for i in range(27)]for j in range(27)],
        elif c=='STOP':
            continue
        else:
            mult=[[i==j for i in range(27)]for j in range(27)]
            pn=[0]*27
            for op,v in zip(*[iter(l)]*2):
                co=1-2*(op=='-')
                if v[0].isdigit():
                    v+='{'
                    j=0
                    while v[j].isdigit():j+=1
                    co*=int(v[:j])
                    v=v[j]
                pn[ord(v)-97]+=co
            for j in range(27):
                mult[j][ord(c)-97]=pn[j]
            block.multblock[-1]=matmul(block.multblock[-1],mult)
        ptr+=1
    return block

ret=parse(s[1:])
var=matmul([[0]*26+[1]],ret.multblock[0])
for p,mult in zip(ret.printblock,ret.multblock[1:]):
    print(p,'=',var[0][ord(p)-97])
    var=matmul(var,mult)