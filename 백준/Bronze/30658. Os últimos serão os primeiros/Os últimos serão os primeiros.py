l=[*map(int,open(0))][::-1]
while n:=int(l.pop()):print(*l[-n:],0);l=l[:-n]