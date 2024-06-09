class R(float):__or__=lambda s,r:R(r*s/(r+s));__sub__=lambda s,r:R(r+s)
_,p,q=open(i:=0)
for j in p.split():i+=1;exec(f'R{i}=R({j})')
print(eval(q))