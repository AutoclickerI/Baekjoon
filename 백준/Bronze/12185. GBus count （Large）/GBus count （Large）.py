for T in range(1,int(input())+1):
    n=int(input())
    *l,=map(int,input().split())
    v=[]
    for _ in[0]*int(input()):
        z=int(input())
        v+=sum(l[2*i]<=z<=l[2*i+1]for i in range(n)),
    print(f'Case #{T}:',*v)
    input()