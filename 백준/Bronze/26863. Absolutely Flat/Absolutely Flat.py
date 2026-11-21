*a,p=map(int,open(0))
a.sort()
a[0]+=p*(a[0]!=a[-1])
print(+(len({*a})<2))