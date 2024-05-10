f=lambda n:n and f(n//19)+str(n%19)or""
print(f(sum(map(int,input().split(),[19,19]))))