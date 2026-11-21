N,K,*l=map(int,open(0).read().split())
m,*l=sorted(l)
print(-(K>=l[-1]and(m<1or~sum((K-i)//m for i in l))))