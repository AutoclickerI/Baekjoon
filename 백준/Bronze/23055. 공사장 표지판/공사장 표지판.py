N=int(input())
for i in range(N):
    if i in[0,N-1]:s=['*']*N
    else:s=[' ']*N;s[0]=s[-1]=s[i]=s[~i]='*'
    print(*s,sep='')