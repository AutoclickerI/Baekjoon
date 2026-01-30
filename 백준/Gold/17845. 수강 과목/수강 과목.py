[N,K],*l=[map(int,i.split())for i in open(0)]
v=[0]*-~N
for I,T in l:
 for i in range(N-T+1):v[~i]=max(v[~i],v[~i-T]+I)
print(v[-1])