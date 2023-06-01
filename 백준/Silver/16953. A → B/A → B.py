n=1
a,b=list(map(int,input().split()))
while a<b:
    if b%10==1:
        b=(b-1)//10
    else:
        if b%2==1:
            b=0
        b//=2
    n+=1
print(n if a==b else -1)