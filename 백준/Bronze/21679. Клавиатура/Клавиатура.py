I=lambda:map(int,input().split())
I()
*l,=I()
I()
for i in I():l[i-1]-=1
for i in l:print('yneos'[i>=0::2])