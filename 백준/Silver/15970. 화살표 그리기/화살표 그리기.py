_,*l=[[*map(int,i.split())]for i in open(0)]
print(sum(sorted(abs(i-p)for p,q in l if q==j)[1]for i,j in l))