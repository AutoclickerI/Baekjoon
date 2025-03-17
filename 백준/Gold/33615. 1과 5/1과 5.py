for _ in[0]*int(input()):
    s=input()
    n=sum(map(int,s))
    if n%3<1:
        print(0,3)
    elif n%3<2:
        v=s.find('1')
        if v<0:
            print(0,5)
        else:
            print(v+1,3)
    else:
        v=s.find('5')
        if v<0:
            print(len(s)%2,11)
        else:
            print(v+1,3)