for _ in[0]*int(input()):
    N,M=map(int,input().split())
    l=[sum(i)for i in zip(*[map(int,input().split())for _ in[0]*M])]
    print(l.index(max(l))+1)