W,*l=open(0)
v=[0]*32
for i in l:
 for j in range(int(W[-3:])+1):v[j]=max(v[j],v[j-1])+(j%2+1==int(i))
print(max(v))