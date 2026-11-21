N=int(input())
d=b'\x07'
a='Impossible'
for i in range(1440):a=[a,'%02d:%02d'%(t:=i//60,m:=i%60)][d[t//10]+d[t%10]+d[m//10]+d[m%10]==N]
print(a)