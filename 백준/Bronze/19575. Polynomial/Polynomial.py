(_,x),*l=[map(int,i.split())for i in open(0)]
v=0
for p,_ in l:v=(v*x+p)%(10**9+7)
print(v)