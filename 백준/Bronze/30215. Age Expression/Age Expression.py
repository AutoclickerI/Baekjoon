p,q,r=map(int,input().split())
a=q
while a<p:
    b=r
    while b<p:
        if a+b==p:
            exit(print(1))
        b+=r
    a+=q
print(0)