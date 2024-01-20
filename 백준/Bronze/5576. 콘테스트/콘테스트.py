*l,=map(int,open(0))
print(*map(sum,[sorted(l[:10])[7:],sorted(l[10:])[7:]]))