*l,=map(int,open(0))
while n:=int(l.pop(0)):print(*l[n-1::-1],0);l=l[n:]