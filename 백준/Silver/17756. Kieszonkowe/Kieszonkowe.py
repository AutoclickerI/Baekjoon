*l,=map(int,[*open(0)][1].split())
a=sum(l)
print(a-min([i for i in l if i*a%2]or[0])or'NIESTETY')