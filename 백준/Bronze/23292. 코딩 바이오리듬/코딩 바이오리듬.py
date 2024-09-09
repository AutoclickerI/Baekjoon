g=lambda p,a,b:sum((int(s[i])-int(p[i]))**2for i in range(a,b))
s,n,*l=open(0)
print(min((-g(i,0,4)*g(i,4,6)*g(i,6,8),i)for i in l)[1])