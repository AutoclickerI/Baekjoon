for c in[0]*int(input()):
    J,N=map(int,input().split())
    l=sorted(eval(input().replace(*' *'))for _ in[0]*N)
    while 0<J:
        c+=1
        J-=l.pop()
    print(c)