(*_,N),*l=[map(int,i.split())for i in open(0)]
for S,P in l:print(S+abs(P-N))