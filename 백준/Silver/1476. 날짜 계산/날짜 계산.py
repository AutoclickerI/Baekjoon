n=1
a=list(map(int,input().split()))
while 1:
    if [(n-1)%15+1,(n-1)%28+1,(n-1)%19+1]==a:
        break
    n+=1
print(n)