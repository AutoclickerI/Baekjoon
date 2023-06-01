for i in range(int(input())):
    a,b=list(map(int,input().split()))
    l=list(map(int,input().split()))
    n=0
    l[b]+=10
    b=l[b]
    while 1:
        k=l.copy()
        k.sort()
        k[-1]%=10
        k.sort()
        if l[0]%10==k[-1]:
            n+=1
            if b==l[0]:
                break
            del l[0]
        else:
            l.append(l[0])
            del l[0]
    print(n)        