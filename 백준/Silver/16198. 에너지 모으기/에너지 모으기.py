N,*W=map(int,open(0).read().split())
v=[]
def backtrack(e):
    if len(W)<3:
        v.append(e)
        return
    for i in range(1,len(W)-1):
        x=W.pop(i)
        backtrack(e+W[i-1]*W[i])
        W[:i]+=x,
backtrack(0)
print(max(v))