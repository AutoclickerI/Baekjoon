for i in[0]*int(input()):
    l=sorted([*map(int,input().split())]for _ in[0]*4)
    l[3],l[2]=l[2],l[3]
    for i in range(-2,3):
        if (l[i-1][0]-l[i][0])**2+(l[i-1][1]-l[i][1])**2!=(l[i+1][0]-l[i][0])**2+(l[i+1][1]-l[i][1])**2:print(0);break
    else:
        le=(l[i-1][0]-l[i][0])**2+(l[i-1][1]-l[i][1])**2
        p,q=l[0]
        r,s=l[2]
        Le=(p-r)**2+(q-s)**2
        p,q=l[1]
        r,s=l[3]
        LE=(p-r)**2+(q-s)**2
        print(+(2*le==Le==LE))