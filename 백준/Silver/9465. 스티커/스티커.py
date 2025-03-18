for _ in[0]*int(input()):
    input()
    a=b=c=0
    for i,j in zip(map(int,input().split()),map(int,input().split())):
        a,b,c=max(b+i,c+i),max(a+j,c+j),max(a,b,c)
    print(max(a,b,c))