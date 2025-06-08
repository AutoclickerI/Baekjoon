n=int(input())
r=2*n+1
i=1
while i**3<=n:
    j=i
    while i*j*j<=n:
        if n%(i*j)<1:r=min(r,i*j+(i+j)*n//i//j)
        j+=1
    i+=1
print(2*r)