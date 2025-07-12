N,*l=open(0)
B=[0]*-~int(N)
for i in l:a,b,c,d=map(int,i.split());z=c==d;B[a]+=(c>d)*3+z;B[b]+=(c<d)*3+z
for a in B[1:]:print(1+sum(a<x for x in B))