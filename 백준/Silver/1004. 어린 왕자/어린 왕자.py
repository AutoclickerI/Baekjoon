for i in range(int(input())):
    a,b,c,d=list(map(int,input().split()))
    n = 0
    for j in range(int(input())):
        p,q,r=list(map(int,input().split()))
        if ((p-a)**2+(q-b)**2<r**2)!=((p-c)**2+(q-d)**2<r**2):
            n+=1
    print(n)