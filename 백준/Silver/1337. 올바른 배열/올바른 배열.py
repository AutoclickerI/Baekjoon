n,*l=map(int,open(0))
print(min(len({*range(i,i+5)}-{*l})for i in l))