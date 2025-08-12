n,p=map(int,input().split())
print(len({n**(i+p)%p for i in range(p)}))