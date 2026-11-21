n,s,t=map(str.split,open(0))
print('YNEOS'[[sum(map(int,s+t))%2,s!=t]['1'in n]::2])