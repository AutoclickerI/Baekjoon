(x,y,X,Y),_,*l=[map(int,i.split())for i in open(0)]
print(min(t+((p-x)**2+(q-y)**2)**.5+((p-X)**2+(q-Y)**2)**.5for p,q,t in l))