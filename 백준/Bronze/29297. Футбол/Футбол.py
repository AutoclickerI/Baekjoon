for _ in[0]*int(input()):
    x,y=map(int,input().split(':'))
    a=0
    for i in range(10):
        for j in range(10):
            a+=x+i>y+j or x+i==y+j and i>y
    print(a,99-a)