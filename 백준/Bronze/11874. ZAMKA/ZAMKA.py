L,D,X=map(int,open(0))
while eval('+'.join(str(L)))-X:L+=1
while eval('+'.join(str(D)))-X:D-=1
print(L,D)