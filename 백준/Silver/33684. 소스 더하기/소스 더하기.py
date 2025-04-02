N,K=map(int,input().split())

m,*l=sorted(map(int,input().split()))

if K<l[-1]:
    print(0)
else:
    if m<1:
        print(-1)
    else:
        print(sum((K-i)//m for i in l)+1)