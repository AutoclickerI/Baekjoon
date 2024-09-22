*l,=map(len,open(0))
n=max(l)
print(sum((n-i)**2for i in l[:-1]))