for _ in[0]*int(input()):
    p,q=map(int,input().split())
    print(sum(int(input())>p for _ in[0]*q))