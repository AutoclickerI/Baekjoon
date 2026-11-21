a,h,B,H=map(int,open(0).read().split())
p,q=-H//a,-h//B
print(f'PLAYER {"AB"[p<q]}'if p-q else'DRAW')