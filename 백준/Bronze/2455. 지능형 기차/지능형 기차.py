m=0
n=0
for i in range(4):
    a,b=list(map(int,input().split()))
    n+=b-a
    if n>m:
        m=n
print(m)