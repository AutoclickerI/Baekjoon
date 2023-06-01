p,q,r=map(int,input().split())
if abs(p-q)<r:
    print((p+q+r)//2*2)
else:
    print(2*(min(p,q)+r))