n,k=map(int,input().split())
t=''
while n:t=str(n%k)+t;n//=k
t=sum(map(int,t.replace(*'0 ').split()))
n=''
while t:n=str(t%k)+n;t//=k
print(n)