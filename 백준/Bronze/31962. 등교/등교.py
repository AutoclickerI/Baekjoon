[N,X],*l=[map(int,i.split())for i in open(0)]
print(max([i for i,j in l if i+j<=X],default=-1))