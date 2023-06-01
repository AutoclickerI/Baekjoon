n=int(input())
a=int(input())
if n==1:
    print(a)
else:
    b=list(map(int,input().split()))
    b[0]+=a;b[1]+=a
    for i in range(n-2):
        c=list(map(int,input().split()))
        c[0]+=b[0];c[-1]+=b[-1]
        for j in range(1,len(c)-1):
            c[j]+=max(b[j-1],b[j])
        b=c
    print(max(b))