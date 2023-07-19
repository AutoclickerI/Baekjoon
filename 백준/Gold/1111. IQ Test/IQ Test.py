n=int(input())
*l,=map(int,input().split())
if len(l)==1:
    print('A')
elif len(l)==2:
    print(['A',l[0]][l[0]==l[1]])
else:
    if l[1]==l[0]:
        if len(set(l))==1:
            print(l[0])
        else:
            print('B')
    else:
        a=(l[2]-l[1])//(l[1]-l[0])
        for b in range(-30000,30000):
            for i,j in zip(l,l[1:]):
                if a*i+b!=j:break
            else:
                print(a*l[-1]+b)
                break
        else:
            print('B')