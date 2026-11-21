def naive(n,C=0):
 while n!=1:C+=n%2+1;n=(n+1)//2
 return C
for i in map(int,[*open(0)][1:]):print(naive(i))