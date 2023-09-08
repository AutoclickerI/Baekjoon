a,b,c,d=map(int,open(0).read().replace(*': ').split())
print('YNEOS'[c>a or d>b::2])