s=open(0).read()
print(*sorted(map(chr,range(65,91)),key=s.index),sep='')