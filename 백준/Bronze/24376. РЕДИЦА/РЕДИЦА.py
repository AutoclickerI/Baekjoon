x,n=map(int,input().split())
s=''
i=0
while len(s)<n:s+=str(x**i);i+=1
print(s[n-1])