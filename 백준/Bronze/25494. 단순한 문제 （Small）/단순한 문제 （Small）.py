for _ in[0]*int(input()):
    p,q,r=map(int,input().split())
    print(sum(i%j==j%k==k%i for i in range(1,p+1)for j in range(1,q+1)for k in range(1,r+1)))