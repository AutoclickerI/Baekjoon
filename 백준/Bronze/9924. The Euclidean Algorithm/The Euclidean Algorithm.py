a,b=map(int,input().split())
c=-1
while b:a,b,c=b,a%b,c+a//b
print(c)