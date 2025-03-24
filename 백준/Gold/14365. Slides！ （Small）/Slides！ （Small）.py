for T in range(1,int(input())+1):
    B,M=map(int,input().split())
    if 2**(B-2)<M:
        print(f'Case #{T}: IMPOSSIBLE')
    else:
        print(f'Case #{T}: POSSIBLE')
        v=[B*[0]for _ in[0]*B]
        for y in range(1,B):
            for x in range(y+1,B):
                v[y][x]=1
        v[0]=f'{min(M,2**(B-2)-1):b}'.zfill(B-1)+'01'[M==2**(B-2)]
        for i in v:
            print(*i,sep='')