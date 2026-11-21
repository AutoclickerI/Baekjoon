x,z,*y=({*i.split()[1:]}for i in open(0))
print(sum(x&i==z for i in y))