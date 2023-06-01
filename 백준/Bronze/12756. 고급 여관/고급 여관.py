a,h,B,H=map(int,open(0).read().split())
p,q=(H-1)//a,(h-1)//B
print(f'PLAYER {"AB"[p>q]}'if p-q else'DRAW')