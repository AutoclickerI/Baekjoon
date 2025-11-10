p,q,_,*l=[[*map(int,i.split())]for i in open(0)]
print(sum(max(sum(max(a-b*n,0)for n in range(c))for a,b,c in(p+i,q+[j]))for*i,j in l))