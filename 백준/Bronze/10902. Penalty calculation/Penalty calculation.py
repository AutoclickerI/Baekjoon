_,*L=map(int,open(0).read().split())
S=L[1::2]
print((S[i:=S.index(max(S))]>0)*(L[::2][i]+20*i))