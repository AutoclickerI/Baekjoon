n=sum(map(int,input().split(),b'  '))
s=''
while n:s=str(n%32)+s;n>>=5
print(s)