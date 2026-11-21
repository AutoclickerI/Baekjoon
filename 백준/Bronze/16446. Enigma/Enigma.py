S,T=open(0)
print(sum(all(x!=y for x,y in zip(S[i:],T[:-1]))for i in range(len(S)-len(T)+1)))