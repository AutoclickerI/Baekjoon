I=input
while n:=int(I()[2:]):l=I();print(eval('+all(i<=j for i,j in zip(I(),l))'*n))