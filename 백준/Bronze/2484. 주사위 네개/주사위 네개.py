def f(l):
    a,b,c,d=l
    if a==b==c==d:
        return 50000+a*5000
    if a==b==c or b==c==d:
        return 10000+b*1000
    if a==b!=c==d:
        return 2000+a*500+c*500
    if a==b or b==c:
        return 1000+b*100
    if c==d:
        return 1000+c*100
    return d*100
print(max(map(f,map(sorted,[map(int,i)for i in map(str.split,[*open(0)][1:])]))))