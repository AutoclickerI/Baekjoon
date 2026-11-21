from statistics import*
n,l=open(0)
l=l.split()
print('YNEOS'[l.count(mode(l))*2>int(n)+1::2])