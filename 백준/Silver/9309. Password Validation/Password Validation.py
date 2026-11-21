def substr(s,t):
    i1=i2=0
    for c in s.lower():
        if t[i1]==c:i1+=1
        if t[~i2]==c:i2+=1
        if max(i1,i2)==len(t):return 1
    return 0

def valid(s):
    ns=[i.lower()for i in s if i not in':!@#$%^&*.,;/?']
    f=1
    f&=8<len(s)<21
    f&=1<sum('`'<i<'{'for i in s)
    f&=1<sum('@'<i<'['for i in s)
    f&=any('/'<i<':'for i in s)
    f&=1<len(s)-len(ns)
    f&=sum(i==j==k for i,j,k in zip(s,s[1:],s[2:]))<1
    f&=1-(ns==ns[::-1])
    f&=1-any(map(substr,[s]*4,['password','virginia','cavalier','code']))
    return f
    

for _ in[0]*int(input()):
    print(['Inv','V'][valid(input())]+'alid Password')