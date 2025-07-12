[N],*l=[map(int,i.split())for i in open(0)]
B=[0]*-~N
for a,b,c,d in l:z=c==d;B[a]+=(c>d)*3+z;B[b]+=(c<d)*3+z
for a in B[1:]:print(1+sum(a<x for x in B))