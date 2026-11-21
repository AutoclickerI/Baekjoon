n,m,*l=map(int,open(0).read().split())
coatis=l[:n]
owls=l[:n-1:-1]
while coatis and owls:
    a = coatis.pop()
    b = owls.pop()
    if a > b:
        a -= (b ** 2 + a - 1) // a
        coatis.append(a)
    elif a < b:
        b -= (a ** 2 + b- 1) // b
        owls.append(b)
if coatis:
    print('coatis',sum(coatis))
elif owls:
    print('owls',sum(owls))
else:
    print('stalemate')
