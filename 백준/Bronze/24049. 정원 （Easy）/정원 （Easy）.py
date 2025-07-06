_,l,v=open(0,'rb')
for i in l:v=[i:=i^j for j in v]
print(v[-2]%2)