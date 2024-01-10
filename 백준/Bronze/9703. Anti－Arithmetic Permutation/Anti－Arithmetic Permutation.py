for k in range(int(input())):
    n=int(input())
    *l,=map(int,input().split())
    f=0
    for i in range(n):
        for j in range(i+1,n):
            for p in range(j+1,n):
                f|=l[i]+l[p]==2*l[j]
    print(f'Case #{k+1}:','YNEOS'[f::2])