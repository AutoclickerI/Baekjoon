X,N=map(int,open(i:=0))
while X<N:X+=[1,X,2*X][X%3];i+=1
print(i)