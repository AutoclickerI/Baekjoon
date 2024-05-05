_,*l=map(int,open(0))
print(min(map(sum,zip(l:=l*2,l[2:]))))