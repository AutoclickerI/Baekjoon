c=r=v=0
for i in[*open(0)][1].split():f=int(i)&1;r+=f;v+=r-r*f;c+=1-f
print(min(v,c*r-v))