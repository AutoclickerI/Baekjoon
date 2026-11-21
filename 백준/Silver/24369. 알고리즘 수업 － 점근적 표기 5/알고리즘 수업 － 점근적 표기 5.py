a,b,c,d,n=map(int,open(0).read().split())
print(+all(d*i<=a*i+c*9801/i+b*99for i in range(n*99,99999)))