n,l=open(0)
n=int(n)
l=l.split()
R=range
print(max(eval('+'.join('*'.join(s)for s in[l[:i],l[i:j],l[j:k],l[k:]]))for i in R(1,n-2)for j in R(i+1,n-1)for k in R(j+1,n)))