for _ in[0]*int(input()):
    N=int(input());l=[[*map(int,input().split())]for _ in[0]*N];a=b=0
    for i in range(N):a+=l[i][i];b+=l[~i][i]
    print(['Not a magic square',f'Magic square of size {N}'][len({a,b,*[sum(i)for i in(*l,*zip(*l))]})<2])