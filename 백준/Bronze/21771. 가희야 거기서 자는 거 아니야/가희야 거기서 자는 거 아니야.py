f=lambda i:map(int,i.split())
p,q,*l=open(0)
R,C=f(p)
a,b,c,d=f(q)
print(+(sum(map(str.count,l,'P'*99))<c*d))