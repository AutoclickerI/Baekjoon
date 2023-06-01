A,B,C,D=map(int,input().split())
for i in map(int,input().split()):
    print(((i-1)%(A+B)+1<=A)+((i-1)%(C+D)+1<=C))