I=input
while"0"<I():*a,=map(int,(I()+" "+I()).split());n=len(a)//2;z=[x<y for i in range(n+1)if(x:=sum(a[:i]))-(y:=sum(a[n:n+i]))];print(sum(x^y for x,y in zip(z,z[1:])))