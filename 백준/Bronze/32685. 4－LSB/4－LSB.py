a,b,c=map(int,open(0))
print(f'{a%16*256+b%16*16+c%16:04}')