for _ in[0]*int(input()):
    input()
    d={}
    s=input()
    for i,v in enumerate(input().split()):
        d[v]=i
    r={}
    for i,v in enumerate(s.split()):
        r[i]=d[v]
    l=input().split()
    for i in range(len(l)):
        print(l[r[i]])