for _ in [0]*int(input()):
    N,K=map(int,input().split())
    print(sum(i//K for i in map(int,input().split())))