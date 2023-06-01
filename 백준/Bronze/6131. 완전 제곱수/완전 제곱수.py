N=int(input())
n=0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if (i+j)*(j-i)==N:
            n+=1
print(n)