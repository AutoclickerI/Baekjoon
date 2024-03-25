for i in[*open(0)][:-1]:
    p,q,r,s=map(int,i.split())
    print(2-(p==r or q==s or abs((p-r)/(q-s))==1)-((p,q)==(r,s)))