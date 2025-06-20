d=[*map(chr,range(65,91)),*'_.']*2
while'0'<(i:=input()):n,s=i.split();print(''.join(d[d.index(c)+int(n)]for c in s[::-1]))