a,b,c,d,e=1,1,1,1,0
v=[(a,b,c,d,e)]
pa=ppa=0
for _ in[0]*100:
    ppa=pa
    pa=a
    a=b+d+e-a+ppa
    b,c,d,e=a+d,a+e,a+b,c
    v+=(a,b,c,d,e),

for i in[*open(0)][1:]:print(v[int(i)][0])