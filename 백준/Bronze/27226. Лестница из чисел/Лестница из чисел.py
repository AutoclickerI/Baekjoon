a,b,k=map(int,open(0))
for i in range(a,b+1):print(*range(j:=~-i*i//2+1,j+min(i,k)))