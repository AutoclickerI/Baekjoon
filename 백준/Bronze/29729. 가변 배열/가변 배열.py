S,N,M,*l=map(int,open(o:=0).read().split())
for i in l:
    o+=2*i-1
    if o>S:S*=2
print(S)