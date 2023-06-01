from math import*
i=0
while sum(l:=[*map(int,input().split())]):
    p,q,r=l
    print(f'Triangle #{(i:=i+1)}')
    try:
        if p==-1:
            ans=sqrt(r*r-q*q)
            if ans==0:raise
            print(f'a = {ans:.3f}')
        elif q==-1:
            ans=sqrt(r*r-p*p)
            if ans==0:raise
            print(f'b = {ans:.3f}')
        else:
            ans=sqrt(p*p+q*q)
            if ans==0:raise
            print(f'c = {ans:.3f}')
    except:
        print('Impossible.')
    print()