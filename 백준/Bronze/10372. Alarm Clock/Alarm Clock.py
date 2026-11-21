N=int(input())
d={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
a='Impossible'
for i in range(1440):
    t=i//60
    m=i%60
    if d[t//10]+d[t%10]+d[m//10]+d[m%10]==N:
        a=f'{t:02}:{m:02}'
print(a)