s={str(i)for i in range(999)if 2<len({*str(i)}-{'0'})}

def chk(g,i):return[v:=sum(map(str.__eq__,g,i)),len({*g}&{*i})-v]

for i in[*open(0)][1:]:
    g,*d=map(int,i.split())
    s={i for i in s if chk(str(g),i)==d}
print(len(s))