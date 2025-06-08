n=int(input())
R=range(1,999)
print(min(z+n//z*(i+j)for i in R for j in R if n%(z:=i*j)<1)*2)