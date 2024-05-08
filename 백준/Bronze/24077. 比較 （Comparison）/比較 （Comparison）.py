n,m,*l=map(int,open(0).read().split())
print(sum(i-j<1for i in l[:n]for j in l[n:]))