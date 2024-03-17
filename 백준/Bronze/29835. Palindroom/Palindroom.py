_,s=open(0)
S=''.join(min(i,j)for i,j in zip(s,s[-2::-1]))
print(sum(i<j for i,j in zip(S,s)),S)