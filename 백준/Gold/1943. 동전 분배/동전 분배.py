for _ in[0]*3:
    N=int(input())
    l=[]
    s=0
    
    for _ in[0]*N:
        a,b=map(int,input().split())
        l+=(a,b),
        s+=a*b
    
    T=s//2
    d=[-1]*-~T
    d[0]=0
    for a,b in l:
        for i in range(T+1):
            if 0<=d[i]:
                d[i]=b
            elif a<=i and 0<d[i-a]:
                d[i]=d[i-a]-1

    print(~s%2*(0<d[T]))