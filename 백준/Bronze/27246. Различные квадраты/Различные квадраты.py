n=int(input())
s=0
while n>0:s+=1;n-=s*s
print(s-(n<0))