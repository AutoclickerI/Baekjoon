c,_,*l=open(0).read()
for i in range(11):
    v=l[i]
    if l[i]=='E':
        l[i]=c
        for z in{*l[:3]},{*l[4:7]},{*l[8:11]},{*l[::4]},{*l[1::4]},{*l[2::4]},{*l[::5]},{*l[2:-1:3]}:
            z=={c}<exit(print(i//4+1,i%4+1))
    l[i]=v