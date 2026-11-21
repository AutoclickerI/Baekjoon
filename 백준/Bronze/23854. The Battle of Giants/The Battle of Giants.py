a,b=map(int,open(0))
print(*[-1]if(a-b)%3else[a//3,a%3,b//3])