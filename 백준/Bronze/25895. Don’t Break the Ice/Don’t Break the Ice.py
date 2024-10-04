for i in range(int(input())):
    n,cnt=map(int,input().split())
    r=[0]*-~n;c=r[:]
    x=0
    for _ in[0]*cnt:a,b=map(int,input().split());x+=r[a]+c[b]>1;r[a]=c[b]=1
    print(f'Strategy #{1+i}: {x}\n')