N,*l=map(int,open(0).read().split())
C=[0]*7**6
for i in l:C[i]+=1
print(N-max(C))