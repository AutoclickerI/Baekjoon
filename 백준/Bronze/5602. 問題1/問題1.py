next(k:=open(0))
print(*[*zip(*sorted(zip(map(lambda x:-x.count('1'),[*zip(*k)][::2]),range(1,999))))][1])