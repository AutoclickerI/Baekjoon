[p,q],_,*l=[map(int,i.split())for i in open(0)]
print(sum(max(p*i,q*j)for i,j in l))