s=input()
k=int(input())
t=min(min(i+j,j+i)for i,j in zip(s,s[1:]))*k
print(t[:k])