n,*l=map(int,open(0).read().split())
print(*min(([max(l[i],l[i+2]),i+1]for i in range(n-2)))[::-1])