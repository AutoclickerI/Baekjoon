for T in range(int(input())):
    print(f'Case #{T+1}:')
    N,Q=map(int,input().split())
    *l,=map(int,input().split())
    l=sorted(sum(l[j:k+1])for j in range(N)for k in range(j,N))
    for _ in[0]*Q:
        s,e=map(int,input().split())
        print(sum(l[s-1:e]))