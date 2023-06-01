s,p=open(0)
r,c=map(int,s.split())
m=p[1]
print([[[min(r,c),max(r,c)][m=="e"],c][m=="u"],r][m=="a"])