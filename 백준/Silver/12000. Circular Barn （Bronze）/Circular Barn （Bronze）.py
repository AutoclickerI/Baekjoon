n,*l=map(int,open(0))
r=range
print(min(sum((j-i)%n*l[j]for j in r(n))for i in r(n)))