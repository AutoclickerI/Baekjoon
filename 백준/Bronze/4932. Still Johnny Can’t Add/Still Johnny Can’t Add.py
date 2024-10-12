for T in range(int(input())):
    n=int(input())
    l=eval('[*map(int,input().split())],'*n)
    f=0
    for i in range(n-1):f|=len({j[i+1]-j[i]for j in l})>1
    print(f'{T+1}.','YNEOS'[f::2])