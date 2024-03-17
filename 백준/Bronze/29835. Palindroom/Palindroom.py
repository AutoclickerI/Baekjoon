input()
s=input()
S=''.join(min(i,j)for i,j in zip(s,s[::-1]))
print(sum(i<j for i,j in zip(S,s)),S)