n=int(input())
s1={1}
s2={1}
for i in range(1,1416):
    if n%i<1:s1|={i,n//i}
    if(n+2)%i<1:s2|={i,(n+2)//i}
for a in s1:
    for b in s2:
        c=n//a
        d=(n+2)//b
        if(n+1)==a*d-b*c:exit(print(a,-b,c,d))
        if(n+1)==b*c-a*d:exit(print(a,b,c,-d))
        if(n+1)==a*b-d*c:exit(print(a,-d,c,b))
        if(n+1)==d*c-a*b:exit(print(a,d,c,-b))
print(-1)