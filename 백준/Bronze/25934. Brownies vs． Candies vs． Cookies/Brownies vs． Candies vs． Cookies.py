for T in range(int(input())):
    s,b=map(int,input().split())
    print(f'Practice #{T+1}:',s,b)
    for _ in[0]*int(input()):
        n=int(input())
        while b<=n:
            b<<=1
        b-=n
        print(n,b)
    print()