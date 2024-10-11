d={}
while'1'<(s:=input()):
    X,Y=map(int,s.split())
    for i in X,Y,-X,-Y,X-Y:
        if i not in d:f=+(i<1);d[i]=f'{f}{i+128*f:07b}'
        print(i,'=',d[i])
    print()