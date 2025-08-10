b=c=0
for i in[*open(0)][1:]:d,e,f=i.split();b+=int(e);g='FDCBA'.find(f[0]);g+=(g>0)and'-0+'.find(f[1])*.3-.3;c+=int(e)*g
print(f'{c/b+1e-4:.2f}')