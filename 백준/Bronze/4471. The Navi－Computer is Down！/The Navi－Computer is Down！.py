for _ in[0]*int(input()):
    s=input()
    *l,=map(eval,input().split())
    e=input()
    *l2,=map(eval,input().split())
    d=sum((i-j)**2 for i,j in zip(l,l2))
    print(s,'to',e+':','%.02f'%d**.5)
    