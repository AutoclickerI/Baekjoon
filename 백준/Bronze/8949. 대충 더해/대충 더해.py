n=sum(map(int,input().split(),b''))
s=''
while n:s=str(n%19)+s;n//=19
print(s)