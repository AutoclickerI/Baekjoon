for i in[*open(n:=0)][1:]:
    p,q=map(int,i.split())
    if p-1:
        n-=q
        if n<0:exit(print('Adios'))
    else:
        n+=q
print('See you next month')