N,K=map(int,input().split())
print(['Your wish is granted!','You will become a flying monkey!'][K<len(f'{N:b}')-(N&N-1<1)])