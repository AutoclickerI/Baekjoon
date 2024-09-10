g=[]
n=0
for _ in[0]*20:
    g+=((2<<n+1)-1,1<<n),
    n+=1
l=[]
for end,length in g:
    l+=range(end-length+1,end+1)
l+=-1,
bi=[0]
ptr=0
for i in range(1,2999999):
    flag=l[ptr]==i 
    bi+=bi[-1]+flag,
    ptr+=flag

def si(n):
    if n<2:
        return 0
    return 1+bi[n-1]

N=int(input())
print(max([1+si(k)+si(N-k-1)for k in range(N//2+1)]))