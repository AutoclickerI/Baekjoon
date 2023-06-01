a,b,c=list(map(int,input().split()))
a=a/(b**2+c**2)**0.5
print(int(a*b),int(a*c))