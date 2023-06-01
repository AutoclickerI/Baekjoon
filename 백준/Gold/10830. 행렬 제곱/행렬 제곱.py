a,b=list(map(int,input().split()))
m=[list(map(int,input().split()))for i in range(a)]
def f(h,z):
    return[[sum([h[i][k]*z[k][j]for k in range(a)])%1000 for j in range(a)]for i in range(a)]
def j(h,q):
    if q==1:
        return h
    l=f(h,h)
    if q%2==0:
        return j(l,q//2)
    return f(j(l,q//2),h)
for g in j(m,b):
    for k in g:
        print(k%1000,end=' ')
    print()