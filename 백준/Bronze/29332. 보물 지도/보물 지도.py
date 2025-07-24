z=[[],[],[],[]]
for i in[*open(0)][1:]:x,y,c=i.split();z[ord(c)%5]+=int((y,x)[c in'LR']),
f=lambda s:min(z[~s])+~max(z[s])
print(f(2)*f(0)if all(z)else'Infinity')