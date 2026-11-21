p,q,r,s=map(int,open(0).read().replace(*'- ').split())
t=p*360+~-q*30+r+s-1
print(f'{t//360}-{t//30%12+1:02}-{t%30+1:02}')