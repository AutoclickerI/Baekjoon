n,m,*a=map(int,open(0).read().split())
d=n*~n//-2-sum(a)
a.insert(d-1,d)
print(f'Yes {d}'*(a==[*range(1,n+1)])or'No')