A,B,N,*l=map(int,open(0).read().split())
print(min(abs(A-B),*[1+abs(i-B)for i in l]))