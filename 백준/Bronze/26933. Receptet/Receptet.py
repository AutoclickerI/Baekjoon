a=0
for i in[*open(0)][1:]:
    p,q,r=map(int,i.split())
    a+=max((q-p)*r,0)
print(a)