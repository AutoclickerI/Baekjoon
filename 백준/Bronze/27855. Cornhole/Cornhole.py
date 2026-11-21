p,q,r,s=map(int,open(0).read()[::2])
p=p*3+q-r*3-s
print(*p and(2-(p>0),abs(p))or['NO SCORE'])