from itertools import*
F=lambda:map(int,input().split())
for T in range(*F()):n,k=F();print(f'Case #{T+1}:',sum(o^p^q^r==k for o,p,q,r in product(*(F()for i in[0]*4))))