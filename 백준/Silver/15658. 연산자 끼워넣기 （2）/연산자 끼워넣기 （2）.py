import sys
sys.setrecursionlimit(9**9)

N,*l,a,s,m,d=map(int,open(0).read().split())
ans=[]
def backtrack(r,i,a,s,m,d):
    if i==N:
        ans.append(r)
        return
    if a:
        backtrack(r+l[i],i+1,a-1,s,m,d)
    if s:
        backtrack(r-l[i],i+1,a,s-1,m,d)
    if m:
        backtrack(r*l[i],i+1,a,s,m-1,d)
    if d:
        sign=-(r<0)|1
        backtrack(abs(r)//l[i]*sign,i+1,a,s,m,d-1)
backtrack(l[0],1,a,s,m,d)
print(max(ans),min(ans))