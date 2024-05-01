p,q,r=map(int,input().split())
l=[p+q,p-q,p*q]+[p//q]*(p%q<1)
t=[]
for p in l:
    t+=[i for i in[p+r,p-r,p*r]+[p//r]*(p%r<1)if i>-1]
print(min(t))