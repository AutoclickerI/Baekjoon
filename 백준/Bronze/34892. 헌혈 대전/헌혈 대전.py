N,A,B,C,D,E,F,G,H=map(int,input().split())
l=[]
for X in range(10001):
    if 1<len(l):break
    for Y in range(10001-X):
        Z=N-X-Y
        if A*X+B*Y+C*Z==D and E*X+F*Y+G*Z==H:
            l+=(X,Y,Z),
if l:
    if 1<len(l):
        print(1)
    else:
        print(0)
        print(*l[0])
else:
    print(2)