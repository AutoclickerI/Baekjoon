_,*l=map(int,open(k:=0).read().split())
while l:
    k+=1;n,W,E,*l=l
    for _ in[H:=0]*n:p,q,r,s,*l=l;H+=max(W*p+E*r,W*q+E*s)
    print(f'Data Set {k}:\n{H}\n')