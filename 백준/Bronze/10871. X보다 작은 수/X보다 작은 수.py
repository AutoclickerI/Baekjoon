N,X=map(int,input().split())
li=list(map(int,input().split()))
r=[]
for i in li:
    if i<X:
        r.append(i)
for i in r:
    print(i,end=' ')