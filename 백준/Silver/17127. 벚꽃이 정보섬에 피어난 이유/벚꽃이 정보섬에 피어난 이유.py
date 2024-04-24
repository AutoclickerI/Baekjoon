n,l=open(0)
n=int(n)
l=l.split()
R=range
print(max(eval('+'.join('*'.join(s)for s in[l[:k],l[k:j],l[j:i],l[i:]]))for i in R(n)for j in R(i)for k in R(1,j)))