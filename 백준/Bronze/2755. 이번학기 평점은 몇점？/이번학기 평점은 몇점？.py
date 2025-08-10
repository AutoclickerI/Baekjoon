b=c=0
for i in[*open(0)][1:]:_,e,f=i.split();e=int(e);b+=e;c+=e*max(0,69-ord(f[0])+'0+'.find(f[-1])*.3)
print(f'{c/b+1e-4:.2f}')