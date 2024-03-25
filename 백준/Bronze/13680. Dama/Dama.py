for i in[*open(0)][:-1]:
    p,q,r,s=map(int,i.split())
    a=2
    if(p,q)==(r,s):a=0
    elif(p==r)or(q==s)or abs((p-r)/(q-s))==1:a=1
    print(a)