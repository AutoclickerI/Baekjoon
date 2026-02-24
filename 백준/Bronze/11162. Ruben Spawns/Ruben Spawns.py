_,*l=map(int,open(0).read().split())
while l:
    W,M,*l=l
    i=0
    for v in sorted(l[:M])[::-1]:
        W-=v
        i+=1
        if W<1:
            print(i)
            break
    else:
        print('no rest for Ruben')
    
    l=l[M:]