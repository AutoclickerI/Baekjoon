[N,Q],*l=[map(int,i.split())for i in open(0)]
c=[a:=0]*-~N
for i in l:
    *s,=i
    if s[0]==1:
        a+=c[s[1]]^1
        c[s[1]]=1
    elif s[0]==2:
        a-=c[s[1]]
        c[s[1]]=0
    else:
        print(N-a)