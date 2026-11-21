N,K=map(int,input().split())
p=0
exec('p+=p//~-K+1;'*~-N)
print(p)