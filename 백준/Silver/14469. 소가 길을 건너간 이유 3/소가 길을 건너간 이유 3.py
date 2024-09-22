a=0
for t,d in sorted([*map(int,i.split())]for i in[*open(0)][1:]):a=max(a,t)+d
print(a)