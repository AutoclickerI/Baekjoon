A,B,C,D=zip(*[map(int,i.split())for i in open(0)][1:])
d1={}
d2={}
for i in A:
    for j in B:
        d1[i+j]=d1.get(i+j,0)+1
a=0
for i in C:
    for j in D:
        a+=d1.get(-i-j,0)
print(a)