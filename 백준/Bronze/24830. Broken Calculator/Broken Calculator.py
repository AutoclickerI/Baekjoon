s=1
for _ in[0]*int(input()):
    p,q,r=input().split()
    p=int(p)
    r=int(r)
    if q=='+':s=p+r-s
    if q=='-':s*=p-r
    if q=='*':s=(p*r)**2
    if q=='/':s=-(p//-2)
    print(s)