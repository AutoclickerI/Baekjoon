I=input
d={}
for _ in[0]*int(I()):p,q=I().split();d[p]=int(q)
print(sum(d.get(I(),0)-10for _ in[0]*int(I())))