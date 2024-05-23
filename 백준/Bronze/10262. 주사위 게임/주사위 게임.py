p,q=map(eval,map(str.replace,open(0),'  ','++'))
print(['Tie','Gunnar','Emma'][(p>q)-(p<q)])