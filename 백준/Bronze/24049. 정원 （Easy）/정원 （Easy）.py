_,l,v=[map(int,i[::2])for i in open(0)]
for i in l:v=[i:=i^j for j in v]
print(i)