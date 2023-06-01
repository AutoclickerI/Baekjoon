multi=lambda a,b:[[sum([a[i][k]*b[k][j]for k in[0,1]])%1000 for j in[0,1]]for i in[0,1]]
cache={}
def DaC(p,q):
    if q==1:
        return p
    if q in cache:
        return cache[q]
    if q%2==0:
        cache[q]=multi(DaC(p,q//2),DaC(p,q//2))
        return multi(DaC(p,q//2),DaC(p,q//2))
    else:
        cache[q]=multi(multi(DaC(p,q//2),DaC(p,q//2)),p)
        return multi(multi(DaC(p,q//2),DaC(p,q//2)),p)
for i in range(int(input())):
    X,Y=DaC([[6,-4],[1,0]],int(input())-1)[1]
    print('Case #{}: {:03d}'.format(i+1,(28*X+6*Y)%1000-1))