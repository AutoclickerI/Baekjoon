from functools import cmp_to_key
N,K=map(int,input().split())
*S,=input()
l=[(i,chr(65+j))for i in range(N)for j in range(26)if chr(65+j)!=S[i]]+[(0,S[0])]
def comp(x,y):
    p,q=x
    r,s=y
    if p==r:
        if q>s:return 1
        if q==s:return 0
        if q<s:return -1
    else:
        if p>r:
            if S[r]>s:return 1
            if S[r]==s:return (q<S[p])*2-1
            if S[r]<s:return -1
        else:
            if q<S[p]:return 1
            if q==S[p]:return (S[r]>s)*2-1
            if q>S[p]:return -1
        
l.sort(key=cmp_to_key(comp))
try:
    p,q=l[K-1]
    *L,=S
    L[p]=q
    print(*L,sep='')
except:print(-1)