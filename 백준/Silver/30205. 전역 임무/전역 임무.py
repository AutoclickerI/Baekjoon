N,M,P=map(int,input().split())
for _ in[0]*N:
    d=0
    for i in sorted(map(int,input().split())):
        if i==-1:
            d+=1
        else:
            while i>P:
                if d==0:
                    exit(print(0))
                d-=1
                P*=2
            P+=i
    P<<=d
print(1)