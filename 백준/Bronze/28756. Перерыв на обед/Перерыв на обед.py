(x,y,X,Y),_,*l=[map(int,i.split())for i in open(0)]
s=x+y*1j
e=X+Y*1j
print(min(t+abs(s-p-q*1j)+abs(e-p-q*1j)for p,q,t in l))