class r:
 def __init__(s,R):s.R=R
 __or__=lambda s,R:r(1/(1/R.R+1/s.R));__sub__=lambda s,R:r(R.R+s.R)
_,p,q=open(0)
for i,j in enumerate(p.split(),1):exec(f'R{i}=r({j})')
print(eval(q).R)