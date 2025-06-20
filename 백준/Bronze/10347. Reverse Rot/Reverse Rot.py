d=*map(chr,range(65,91)),*'_.'
while'0'<(i:=input()):n,s=i.split();print(''.join(d[d.index(c)+int(n)-28]for c in s[::-1]))