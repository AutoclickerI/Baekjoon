for i in range(int(input())):
    a=input().split();a[0]=float(a[0])
    for i in range(1,len(a)):
        if a[i]=='@':
            a[0]*=3
        if a[i]=='#':
            a[0]-=7
        if a[i]=='%':
            a[0]+=5
    print('{:.2f}'.format(a[0]))