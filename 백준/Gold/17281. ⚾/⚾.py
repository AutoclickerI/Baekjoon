_,*l=[[*map(int,i.split())]for i in open(0)]

from itertools import*

m=0

for i in permutations(range(1,9)):
    c=[*i[:3],0,*i[3:]]
    o=s=0
    for i in l:
        p=[]
        out=0
        while out<3:
            v=i[c[o%9]]
            if v==0:
                out+=1
            if v==1:
                p+=1,
            if v==2:
                p+=1,0
            if v==3:
                p+=1,0,0
            if v==4:
                s+=sum(p)+1
                p=[]
            o+=1
        s+=sum(p[:-3])
    m=max(m,s)
print(m)