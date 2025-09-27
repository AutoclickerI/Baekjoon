n=b=0
a=[0]*99
for s in open(0):
 i=0
 for j in s:a[i]+='!'<j*b;i+=1
 b|=1<s.count('#');n+=b<1
print(n,*filter(int,a))