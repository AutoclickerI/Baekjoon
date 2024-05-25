N,_,*l=map(int,open(0).read().split())
a={0}
for K in l:a|={K*-~i for i in range(N//K)}
print(sum(a))