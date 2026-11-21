n,m=map(int,input().split())
i=a=0
b=1
while i<m:i+=1;a,b=b,(a+b)%10;n<=i!=print(a,end='')