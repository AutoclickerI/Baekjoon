f=lambda:sorted(map(int,input().split()))
print(sum(i*j for i,j in zip(f(),f())))