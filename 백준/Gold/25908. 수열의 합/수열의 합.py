s,e=map(int,input().split())
f=lambda n:sum(n//(i+1)*(i%2*2-1)for i in range(n))
print(f(e)-f(s-1))