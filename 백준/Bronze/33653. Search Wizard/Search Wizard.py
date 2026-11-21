S,_,T=open(0)
print(sum(S[:-1]==T[i:i+len(S)-1]for i in range(len(T))))