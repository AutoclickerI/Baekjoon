_,*l=map(int,open(c:=0))
n=30
for i in l:
    if i<=n:
        n-=i
        c+=1
        if n==0:
            n=30
    else:
        c+=i<=n*2
        n=30
print(c)