a=int(input())
n=64
x=0
while a>0:
    if a>=n:
        a-=n
        x+=1
    else:
        n//=2
print(x)