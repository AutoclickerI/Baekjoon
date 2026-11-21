*l,=map(iter,open(0,'rb').read().split()[1:])
c=1
while c:
    c=v=0
    for i in l:
        try:v+=next(i);c+=1
        except:0
    if c:print(end=chr(v//c))