a,b,c,d,e,f=map(int,open(0).read().split())
if a==c:
    if a!=e or max(b,d)<f or f<min(b,d):
        print(0)
    else:
        print(2)
elif b==d:
    if b!=f or max(a,c)<e or e<min(a,c):
        print(0)
    else:
        print(2)
else:
    print(1)