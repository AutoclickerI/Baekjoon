(x,y,X,Y),_,*l=[map(int,i.split())for i in open(0)]
print(min(t+abs(x-p+(y-q)*1j)+abs(X-p+(Y-q)*1j)for p,q,t in l))