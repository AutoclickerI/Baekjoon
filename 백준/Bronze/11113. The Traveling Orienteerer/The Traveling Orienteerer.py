[n],*l=map(str.split,open(0))
n=int(n)
p=[eval(i+'j+'+j)for i,j in l[:n]]
for i in l[n+2::2]:print(round(sum(abs(p[int(j)]-p[int(k)])for j,k in zip(i,i[1:]))))