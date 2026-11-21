n=int(input())
s=0
while n>0:n-=(s:=s+1)*s
print(s-(n<0))