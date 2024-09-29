*l,=map(int,input().split())
i=l.index(20)
s1=(l[i]+l[(i+1)%20]+l[i-1])*20
s2=sum(l)*3
if s1==s2:print('Tie')
elif s1>s2:print('Alice')
else:print('Bob')