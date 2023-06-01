p,q,r,s,t,u=map(int,open(0).read().split())
print('YNEOS'[(p-s)**2+(q-t)**2>=(r+u)**2::2])