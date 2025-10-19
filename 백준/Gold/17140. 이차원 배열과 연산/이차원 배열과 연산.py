r,c,k=map(int,input().split())
A=[[*map(int,input().split())]for _ in[0]*3]

r-=1
c-=1

def sort(a):
    d={}
    for i in a:
        d[i]=d.get(i,0)+1
    if 0 in d:del d[0]
    ret=[]
    for i in sorted(d,key=lambda i:(d[i],i)):
        ret+=i,d[i]
    return ret

t=0
while t<101:
    if r<len(A) and c<len(A[0]) and A[r][c]==k:
        exit(print(t))
    t+=1
    f=len(A)<len(A[0])
    if f:
        *A,=zip(*A)
    A=[sort(i)[:100]for i in A]
    ml=max(len(i)for i in A)
    A=[i+[0]*(ml-len(i))for i in A]
    if f:
        *A,=zip(*A)
print(-1)