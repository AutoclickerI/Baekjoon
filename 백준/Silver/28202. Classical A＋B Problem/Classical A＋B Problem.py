for _ in[0]*int(input()):
    s=input()
    #case1
    n=s[0]*len(s)
    n2=str(int(s)-int(n))
    if len({*n})==len({*n2})==1 and {*n}!={'0'}!={*n2}:
        print(n,n2)
    else:
        n='1'*len(n)
        n2=str(int(s)-int(n))
        if len({*n})==len({*n2})==1 and {*n}!={'0'}!={*n2}:
            print(n,n2)
        else:
            n=str(int(s[0])-1)*len(n)
            n2=str(int(s)-int(n))
            if len({*n})==len({*n2})==1 and {*n}!={'0'}!={*n2}:
                print(n,n2)
            else:
                n='9'*(len(s)-1)
                n2=str(int(s)-int(n))
                if len({*n})==len({*n2})==1 and {*n}!={'0'}!={*n2}:
                    print(n,n2)