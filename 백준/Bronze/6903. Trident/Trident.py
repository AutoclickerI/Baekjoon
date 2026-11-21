p,q,r=map(int,open(0))
print(*[(' '*q).join('***')]*p+['*'*(3+2*q)]+[' '*q+' *']*r,sep='\n')