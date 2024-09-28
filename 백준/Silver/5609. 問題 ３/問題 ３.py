a=1
t,d,f,b,l,r=1,6,2,5,4,3
for i in[*open(0)][1:]:t,d,f,b,l,r=[(f,b,d,t,l,r),(b,f,t,d,l,r),(r,l,f,b,t,d),(l,r,f,b,d,t),(t,d,r,l,f,b),(t,d,l,r,b,f)]['NSWERL'.find(i[0])];a+=t
print(a)