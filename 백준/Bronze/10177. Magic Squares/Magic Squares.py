for _ in[0]*int(input()):
    N=int(input())
    l=[[*map(int,input().split())]for _ in[0]*N]
    a=b=0
    for i in range(N):a+=l[i][i];b+=l[~i][i]
    if len({a,b,*[sum(i)for i in(*l,*zip(*l))]})<2:
        print('Magic square of size',N)
    else:
        print('Not a magic square')