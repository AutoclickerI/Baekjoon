for _ in[0]*int(input()):
    p=[ord(i)-65 for i in input()]
    v=[0]*26
    d={}
    for i in range(26):
        if v[i]<1:
            c=1
            while v[i]<1:
                v[i]=1
                i=p[i]
                c+=1
            if c%2:
                d[c]=d.get(c,0)^1
    print('YNeos'[any(d.values())::2])