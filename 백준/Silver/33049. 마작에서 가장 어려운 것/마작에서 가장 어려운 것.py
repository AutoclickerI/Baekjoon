a,b,c=map(int,input().split())

for i in range(c,-1,-1):
    if (a+c-i)%3<1>(b+i)%4:
        break
else:
    exit(print(-1))
print((a+c-i)//3,(b+i)//4)