import random
random.seed(42)
block_size=26
perms_n=[0,20,31,46,58,73,85,99,112,123,138,150,165,177,191,204]
perms=[]
perms_inv=[]
for i in perms_n:
    perms+=[*range(i)],
    random.shuffle(perms[-1])
    permute_inv=[0]*i
    for vv in range(i):
        permute_inv[perms[-1][vv]]=vv
    perms_inv+=permute_inv,

def reorder(l,i):
    if len(l)<2:
        return l
    o=[]
    z=[]
    for v in l:
        if'0'<v[i]:
            o+=v,
        else:
            z+=v,
    if len(o)<len(z):
        return reorder(o,i+1)+reorder(z,i+1)
    else:
        return reorder(z,i+1)+reorder(o,i+1)

def read_bit(i,restore=False):
    if bits[i]==-2:
        qi=perms_inv[N][i]
        print('?',qi+1)
        n=int(input())
        bits[i]=n
    if bits[i]==-1:
        if restore:
            return-1
        hamming[i].restore()
    return bits[i]

class hamming_storage:
    def __init__(self,size,data=None):
        global cnt
        pairity=0
        while 2**pairity<=size+pairity:
            pairity+=1
        self.pairity=pairity
        self.size=size
        self.data_idx=[*range(cnt,cnt+size)]
        cnt+=size
        self.data=data
    def add_pairity(self):
        global cnt
        self.pair_idx=[*range(cnt,cnt+self.pairity)]
        cnt+=self.pairity
        if self.data:
            data=self.data[:]
            for i in range(self.pairity):
                data[:2**i-1]+=0,
            xor=0
            for i in range(len(data)):
                xor^=(i+1)*data[i]
            *self.pair_data,=map(int,f'{xor:b}'.zfill(self.pairity)[::-1])
        
    def restore(self):
        data=[read_bit(i,restore=True)for i in self.data_idx]
        pairity=[read_bit(i,restore=True)for i in self.pair_idx]
        for i in range(self.pairity):
            data[:2**i-1]+=pairity[i],
        minus=[]
        for i in range(len(data)):
            if data[i]==-1:
                minus+=i,
        for i in range(2**len(minus)):
            t=[]
            for _ in[0]*len(minus):
                t+=i%2,
                i//=2
            for idx,val in zip(minus,t):
                data[idx]=val
            xor=0
            for i in range(len(data)):
                xor^=(i+1)*data[i]
            if xor==0:
                break
        pairity=[]
        for i in range(self.pairity)[::-1]:
            pairity+=data.pop(2**i-1),
        for i in range(self.pairity):
            bits[self.pair_idx[i]]=pairity[i]
        for i in range(self.size):
            bits[self.data_idx[i]]=data[i]

if'1'<input():
    for _ in[0]*int(input()):
        X,Q=map(int,input().split())
        cnt=0
        bits=[-2]*X
        N=[0,20,31,46,58,73,85,99,112,123,138,150,165,177,191,204].index(X)
        hamming=[]
        total_bits=[0,15,26,37,48,59,70,81,92,103,114,125,136,147,158,169][N]
        db=[]
        while total_bits:
            n=min(block_size,total_bits)
            total_bits-=n
            db+=hamming_storage(n),
            for _ in[0]*n:
                hamming+=db[-1],
        for i in db:
            i.add_pairity()
        s=0
        e=N
        cnt0=read_bit(0)*8+read_bit(1)*4+read_bit(2)*2+read_bit(3)
        cnt1=N-cnt0
        i=0
        if cnt0==0:
            Q^=1<<11
        elif cnt1==0:
            pass
        else:
            if cnt1<cnt0:
                j=cnt1
                sv=1
            else:
                j=cnt0
                sv=0
            if Q&(1<<11):
                if sv==1:
                    s=j
                else:
                    e=j
            else:
                Q^=1<<11
                if sv==1:
                    e=j
                else:
                    s=j
        for i in range(1,12):
            stoe=e-s
            maxi=stoe//2
            sv=read_bit(i*N+s+4-N)
            ev=read_bit(i*N+(e-1)+4-N)
            if sv==ev:
                for vv in range(s,e):
                    bits[i*N+vv+4-N]=sv
                Q^=sv<<11-i
            else:
                j=s
                bi_s=s
                bi_e=s+maxi
                while 1<bi_e-bi_s:
                    mid=bi_s+bi_e>>1
                    v=read_bit(i*N+mid+4-N)
                    if v==sv:
                        bi_s=mid
                    else:
                        bi_e=mid
                for vv in range(s,bi_s+1):
                    bits[i*N+vv+4-N]=sv
                for vv in range(bi_s+1,e):
                    bits[i*N+vv+4-N]=ev
                for j in range(s,e):
                    if bits[i*N+j+4-N]!=sv:
                        break
                if Q&(1<<11-i):
                    if sv==1:
                        s=j
                    else:
                        e=j
                else:
                    Q^=1<<11-i
                    if sv==1:
                        e=j
                    else:
                        s=j
        print('!',Q)
else:
    for _ in[0]*int(input()):
        input()
        l=reorder([*{f'{int(i):012b}'for i in input().split()}],0)

        N=len(l)
        cnt=0

        db=[]
        l=''.join(''.join(i)for i in zip(*l))
        starting=l[:N]
        cnt0=f'{starting.count("0"):04b}'
        l=cnt0+l[N:]
        X=[*map(int,l)]
        total_bits=len(l)
        
        while total_bits:
            n=min(block_size,total_bits)
            total_bits-=n
            db+=hamming_storage(n,[*map(int,l[:n])]),
            l=l[n:]
        for i in db:
            i.add_pairity()
        for i in db:
            X+=i.pair_data
        print(cnt)
        print(*[X[i]for i in perms[N]])