d={1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6,0:6}
l=[[],[9999999999999999999999]]
for i in range(2,101):
    t=None
    for j in range(10):
        if 0<=i-d[j]:
            nt=l[i-d[j]]+[j]
            nt.sort()
            if nt[-1]<1:
                continue
            *nt,=nt.pop(nt.index(min(filter(int,nt)))),*nt
            if t==None:
                t=nt
            else:
                tn=int(''.join(map(str,t)))
                ttn=int(''.join(map(str,nt)))
                if ttn<tn:
                    t=nt
    l+=t,
for i in[*open(0)][1:]:
    n=int(i)
    print(*l[n],' ','17'[n%2]+'1'*(n//2-1),sep='')