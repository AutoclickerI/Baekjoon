n,*l=open(0)
n=int(n)
s=sum(i.count('C')for i in l)//2
for i in range(n):
 a=''
 for j in range(n):a+='12'[s>0];s-=l[i][j]=='C'
 print(a)