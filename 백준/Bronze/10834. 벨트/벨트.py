r=1
for i in[*open(d:=0)][1:]:a,b,c=map(int,i.split());r=r*b//a;d^=c
print(d,r)