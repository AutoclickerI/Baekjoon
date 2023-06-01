for _ in[0]*int(input()):
    a=b=0
    for i in[0]*int(input()):
        p,q=input().split()
        a+=int(p);b+=float(q)*int(p)
    print(a,b/a)