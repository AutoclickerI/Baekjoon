n,d=map(int,input().split())
l=[]
for _ in[0]*n:
    p,q=map(int,input().split())
    l+=(d-p)/(q+1e-9),
print(l.index(min(l))+1)