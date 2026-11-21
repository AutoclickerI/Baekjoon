a,b=map(int,input().split())
i=1+(a>b)
while a/b**(1/i)<i<=a:i+=1
print(i+~i*(i>a))