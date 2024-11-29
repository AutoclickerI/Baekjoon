a,b=map(int,input().split())
i=1+(a>b)
while 1/b**(1/i)<i/a<=1:i+=1
print(i+~i*(i>a))