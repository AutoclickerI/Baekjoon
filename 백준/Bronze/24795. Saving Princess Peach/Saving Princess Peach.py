N,Y,*l=map(int,open(0).read().split())
print(*{*range(N)}-{*l},'Mario got',len({*l}),'of the dangerous obstacles.')