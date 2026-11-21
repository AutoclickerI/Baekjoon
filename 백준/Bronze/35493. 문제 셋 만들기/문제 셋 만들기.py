n,s=open(0,'rb')
print('YNEOS'[int(n)-s[-2]%2<1::2])