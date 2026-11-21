n,*l=open(0)
n=int(n)
s=sum(i.count('C')for i in l)//2
a=''
for i in range(n*n):a+='12'[s>0]+'\n'*(~i%n<1);s-=l[i//n][i%n]<'D'
print(a)