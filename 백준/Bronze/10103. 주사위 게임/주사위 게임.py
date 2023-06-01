a=b=100
for _ in[0]*int(input()):
    p,q=map(int,input().split())
    if p>q:b-=p
    elif p<q:a-=q
print(a,b)