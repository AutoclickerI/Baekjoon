while'1'<(s:=input()):
    n,s=s.split();m=[];print(s)
    for i in range(int(n)):a,b,c=input().split();m+=[(a,b[0]!='s',float(c))]
    for x,y,z in m:print(f'{x}:',*l if(l:=[i for i,j,k in m if y!=j and[z<=k,k<=z][y]])else['NO-ONE'])