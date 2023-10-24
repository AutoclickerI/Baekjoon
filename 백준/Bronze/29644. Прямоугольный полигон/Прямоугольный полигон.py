S,P=map(int,input().split())
for i in range(300001):
    j=P//2-i
    if(i+j)*2==P and i*j==S:
        exit(print(j,i))
print(-1)