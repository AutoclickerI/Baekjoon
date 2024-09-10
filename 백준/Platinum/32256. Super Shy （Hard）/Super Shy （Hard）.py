g=[]
n=0
for _ in[0]*60:
    g+=((2<<n+1)-1,1<<n),
    n+=1

def bi(n):
    ans=0
    for end,length in g:
        if end<n:
            ans+=length
        elif end-length<n:
            ans+=n-end+length
    return ans

def si(n):
    if n<2:
        return 0
    return 1+bi(n-1)

def f(k):
    if N-k-1<0:
        return 0
    return 1+si(k)+si(N-k-1)
for i in[*open(0)][1:]:
    N=int(i)
    print(max([f(k)for k in[0,N//2,1<<N.bit_length()-1]]))