f=lambda n:n and f(n>>5)+str(n%32)or''
print(f(sum(map(int,input().split(),b'  '))))