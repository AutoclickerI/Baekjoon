N,Y,*l=map(int,open(0).read().split())
print(*sorted({*range(N)}-{*l}),f'Mario got {len({*l})} of the dangerous obstacles.',sep='\n')