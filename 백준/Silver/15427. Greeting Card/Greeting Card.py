d={tuple(map(int,i.split()))for i in[*open(0)][1:]}
a,b=1118,1680
print(sum((i+k,j+l)in d for i,j in d for k,l in zip([a,b]*2+[2018,0],[-b,a,b,-a,0,2018])))