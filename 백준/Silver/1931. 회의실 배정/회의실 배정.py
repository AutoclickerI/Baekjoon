t=-1
print(sum(b>t-1<(t:=a)for a,b in sorted([*map(int,x.split()),t][1::t]for x in open(0)))-1)