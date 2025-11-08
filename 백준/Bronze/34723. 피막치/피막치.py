P,M,C,X=map(int,open(0).read().split())
print(min(abs((i//M//C+i%M+2)*(i%M+i//M%C+2)-X)for i in range(P*M*C)))