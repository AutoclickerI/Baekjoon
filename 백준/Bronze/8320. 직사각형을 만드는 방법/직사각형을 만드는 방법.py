s=set()
n=int(input())
for i in range(1,n+1):
    for j in range(i,n+1):
        if i*j<=n:
            s.add((i,j))
print(len(s))