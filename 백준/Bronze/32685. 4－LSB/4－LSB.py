a,b,c=map(int,open(0))
print(f'{a%16<<8|b%16<<4|c%16:04}')