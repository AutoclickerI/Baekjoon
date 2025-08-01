*l,=map(int,[*open(0)][1].split())
print([s:=sum(l),max(i%2*(s-i)for i in l)][s%2])