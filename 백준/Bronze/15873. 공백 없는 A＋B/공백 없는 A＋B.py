a=list(map(int,list(input())))
print(20 if len(a)==4 else sum(a)if len(a)==2 else 10+a[2]if a[1]==0 else 10+a[0])