l,d,x=map(int,open(0))
a=[i for i in range(l,d+1)if x==sum(map(int,str(i)))]
print(a[0],a[-1])