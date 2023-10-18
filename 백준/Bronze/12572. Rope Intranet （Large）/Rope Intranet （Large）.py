for I in range(int(input())):
    n=int(input())
    X,Y=zip(*[map(int,input().split())for _ in[0]*n])
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            ans+=(X[i]-X[j])*(Y[i]-Y[j])<0
    print(f'Case #{I+1}:',ans)