s=input()
print(sum(i!=j for i,j in zip(s,s[1:]))+1>>1)