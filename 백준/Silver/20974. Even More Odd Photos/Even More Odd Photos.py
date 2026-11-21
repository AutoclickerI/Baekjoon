a=[0,0]
for c in[*open(0)][1].split():a[int(c)&1]+=1
e,o=a
t=max(0,(o-e+2)//3)
o-=t*2
print(o+min(o+1,e+t))