p,m=map(int,input().split())
l=[]
r=[]
for _ in[0]*p:
    lv,s=input().split()
    for i in range(len(l)):
        if l[i]-10<=int(lv)<=l[i]+10 and len(r[i])<m:
            r[i]+=(lv,s),
            break
    else:
        l+=int(lv),
        r+=[[lv,s]],
for i in r:
    if len(i)==m:
        print('Started!')
    else:
        print('Waiting!')
    for v in sorted(i,key=lambda s:s[1]):
        print(*v)