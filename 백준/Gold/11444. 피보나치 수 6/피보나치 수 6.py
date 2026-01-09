p=10**9+7
def f(h,z):
    return[[sum([h[i][k]*z[k][j]for k in range(len(z))])%p
            for j in range(len(z[0]))]for i in range(len(h))]
def j(h,q):
    if q==1:
        return h
    l=f(h,h)
    if q%2==0:
        return j(l,q//2)
    return f(j(l,q//2),h)

n=int(input())

mat=[[0,1],[1,1]]
start=[[0],[1]]

matn=j(mat,n)
res=f(matn,start)

print(*res[0])