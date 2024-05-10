*l,=map(int,open(0))
print(max(sum((l[i:]+l[:i])[:4])for i in range(8)))