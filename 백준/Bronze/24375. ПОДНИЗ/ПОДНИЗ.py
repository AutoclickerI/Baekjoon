p,q=open(0)
for c in range(26):print(end=min(p.count(c:=chr(97+c)),q.count(c))*c)