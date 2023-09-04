*l,=map(int,[*open(0)][1].split())
s=sum(l)
print(sum(i*(s:=s-i)for i in l))