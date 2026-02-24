for _ in[0]*int(input()):
    W,M=map(int,input().split())
    C=sorted(map(int,input().split()))[::-1]
    i=0
    for v in C:
        W-=v
        i+=1
        if W<1:
            print(i)
            break
    else:
        print('no rest for Ruben')