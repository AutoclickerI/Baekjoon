from itertools import*
n,m,d,*k=open(0).read().split()
print(sum(max(len([*w])-int(d)+1,0)for i in k+[*zip(*k)]for v,w in groupby(i)if'#'<v))