n,*l=[eval(i.replace(' ','+1j*'))for i in open(0)]
print(sum(abs(i-j)for i in l for j in l)/n)