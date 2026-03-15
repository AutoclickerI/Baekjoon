_,*l,s=open(0)

d={}
for i,v in enumerate(s.split()):
    if v in d:
        print('Impossible')
        exit()
    d[v]=i

try:
 for i in l:
    b=[]
    for v in i.split():
        if v in d:
            b+=d[v],
            del d[v]
        else:
            raise
    if b!=sorted(b):
        print('Impossible')
        break
 else:
    if d:
        print('Impossible')
    else:
        print('Possible')
except:
    print('Impossible')