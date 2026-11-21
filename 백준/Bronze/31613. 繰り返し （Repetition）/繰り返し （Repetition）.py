X,N=map(int,open(i:=0))
while X<N:X+=X%3*X or 1;i+=1
print(i)