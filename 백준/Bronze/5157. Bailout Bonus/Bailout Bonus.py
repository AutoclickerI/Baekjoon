for i in range(int(input())):
    p,q,r,s=map(int,input().split())
    a=0
    *l,=map(int,input().split())
    for _ in[0]*r:
        p,q=map(int,input().split())
        if p in l:a+=q*s//100
    print(f'Data Set {i+1}:\n{a}\n')