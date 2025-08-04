v=[*open(0)][1].split()
m=max(map(v.count,{*v}-{'0'}))
l=[i for i in{*v}-{'0'}if v.count(i)==m]
print(l[0]if len(l)==1 else'skipped')