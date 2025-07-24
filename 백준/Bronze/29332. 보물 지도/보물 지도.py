z=[[],[],[],[]]
for i in[*open(0)][1:]:x,y,c=i.split();z[ord(c)%5]+=int((y,x)[c in'LR']),
f=lambda s,e:min(z[s])+~max(z[e])
print(f(1,2)*f(3,0)if all(z)else'Infinity')