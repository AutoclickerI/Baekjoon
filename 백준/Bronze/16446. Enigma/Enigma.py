S,T=input(),input()
print(sum(all(x!=y for x,y in zip(S[i:],T))for i in range(len(S)-len(T)+1)))