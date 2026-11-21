I=lambda:map(int,input().split())
N,K=I()
*l1,=I()
*l2,=I()
a=sum(i==j for i,j in zip(l1,l2))
def recur(l,depth):
    global a
    a=max(a,sum(i==j for i,j in zip(l1,l)))
    if depth==0:return
    for i in range(N):
        tmp=l+[0]
        tmp.pop(i)
        recur(tmp,depth-1)
        tmp=l[:]
        tmp.insert(i, 0)
        recur(tmp,depth-1)
recur(l2,K)
print(a)