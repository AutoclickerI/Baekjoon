f=lambda:map(int,input().split())
f()
print(sum(3*(i>j)+(i==j)for i,j in zip(f(),f())))