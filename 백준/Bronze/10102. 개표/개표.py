N,S=open(0)
N=int(N)
S=S.count('A')*2
print(['Tie','AB'[N>S]][N!=S])