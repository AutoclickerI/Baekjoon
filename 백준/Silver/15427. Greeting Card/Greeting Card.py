d={tuple(map(int,i.split()))for i in[*open(0)][1:]}
a,b,c=1118,1680,2018
print(sum((i+k,j+l)in d for i,j in d for k,l in zip([a,b]*2+[c,0],[-b,a,b,-a,0,c])))