*p,=map(int,input().split())
s=[0,0]
c=p[0]>p[1]
for i in range(p[c]):s[c]+=1;print(*s,sep=':')
c^=1
for i in range(p[c]):s[c]+=1;print(*s,sep=':')