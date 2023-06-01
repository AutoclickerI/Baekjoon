a=b=0
for _ in[0]*int(input()):
    for i in[0]*9:
        p,q=map(int,input().split())
        a+=p;b+=q
    if a==b:print('Draw')
    if a>b:print('Yonsei')
    if a<b:print('Korea')
