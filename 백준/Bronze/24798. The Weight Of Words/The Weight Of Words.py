l,w=map(int,input().split())
a=' abcdefghijklmnopqrstuvwxyz'
if 26*l<w or w<l:print('impossible')
else:
    d=w//l
    r=w-d*l
    print(a[d]*(l-r)+(a[d+1]*r if r else''))