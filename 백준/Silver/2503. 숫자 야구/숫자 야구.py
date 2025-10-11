s={str(i)for i in range(999)if 2<len({*str(i)}-{'0'})}

def chk(g,i):
    strike=sum(map(str.__eq__,g,i))
    return[str(strike),str(len({*g}&{*i})-strike)]

for i in[*open(0)][1:]:
    g,*d=i.split()
    s={i for i in s if chk(g,i)==d}
print(len(s))