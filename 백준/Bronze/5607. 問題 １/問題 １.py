a=b=0
for _ in[0]*int(input()):
    p,q=map(int,input().split())
    if p>q:a+=p+q
    elif p<q:b+=p+q
    else:a+=p;b+=q
print(a,b)