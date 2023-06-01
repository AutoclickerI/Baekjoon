import sys
for _ in[0]*int(input()):
    s=p=2100;e=2400
    c=sus=1
    l=[]
    while s<e-1:
        m=(s+e)//2
        print('?',m)
        sys.stdout.flush()
        if input()=='0':
            if sus:
                if s in l:
                    e=m
                    l+=[s]
                else:
                    print('?',s)
                    sys.stdout.flush()
                    if input()=='0':
                        sus=0
                        e=s
                        s=p
                    else:
                        e=m
                        l+=[s]
            else:
                e=m
        else:
            if sus:
                p=s
                s=m
            else:
                s=m
    if sus:
        print('?',s)
        sys.stdout.flush()
        if input()=='1':
            print('!',s)
        else:
            print('!',s-1)
    else:
        print('!',s)
    sys.stdout.flush()