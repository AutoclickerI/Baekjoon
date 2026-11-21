a=b=A=1
c=B=C=0
exec('a,b,c=a+b+c,a,b;A,B,C=A+B+C+a,A,B;'*int(input()))
print(A%10**6)