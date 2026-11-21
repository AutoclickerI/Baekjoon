n,a,b,*s=map(int,open(0).read().split())
print(*range([b,a][b in s],[a,b][a in s]+1)or[-1])