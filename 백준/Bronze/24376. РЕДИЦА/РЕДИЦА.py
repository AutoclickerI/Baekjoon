x,n,*s=map(int,input().split())
i=1
while len(s)<n:s+=str(i:=i*x)
print(s[n-2])