(N,S,K),*l=[map(eval,i.split())for i in open(0)]
i=1
a=0
for m,s in*l,(N+1,S):a+=(m-i)*240/S;i,S=m,s
print(a)