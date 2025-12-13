f=lambda n:n*(n<7)or(x:=4-(n in(7,11,15)))*f(n+~x)
print(f(int(input())))