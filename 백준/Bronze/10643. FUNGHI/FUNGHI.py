l=[*map(int,open(0))]*2
print(max(sum(l[i:][:4])for i in range(8)))