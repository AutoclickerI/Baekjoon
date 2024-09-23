(n,_,t),[*a],z=[map(int,i.split())for i in open(0)]
print(sum(a[n%2:]),n%2*sum(i<=t for i in z))