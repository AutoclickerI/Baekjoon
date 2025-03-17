s=input()
print(*[i*(i==j)for i,j in zip(s,s[1:])],sep='')