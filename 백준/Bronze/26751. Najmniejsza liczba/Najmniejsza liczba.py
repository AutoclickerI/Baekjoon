X,Y,Z=sorted(input().split(),key=int)
if'0'<X:print(X+Y+Z)
elif'0'<Y:print(Y+X+Z)
else:print(Z+'00')