print(sum(a>b for a,b in zip(*map(sorted,map(str.split,open(0))))))