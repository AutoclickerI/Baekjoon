_,p,*l=[map(int,i.split())for i in open(0)]
print(sum(max(i*(e-s),0)for i,(s,e)in zip(p,l)))