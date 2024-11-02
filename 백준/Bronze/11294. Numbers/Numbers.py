i=input
f=lambda n:n and f(n//b)+[str(x:=n%b),chr(55+x)][x>9]or''
while(a:=i())>'#':b=int(i());print(a,c:=int(i()),f(c),sep=', ')