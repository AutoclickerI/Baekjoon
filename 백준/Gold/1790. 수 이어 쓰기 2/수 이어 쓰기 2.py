N,k=map(int,input().split())
i=0
while(t:=9*10**i*(i:=i+1))<k:k-=t
t=10**~-i+~-k//i
print(-(N<t)or str(t)[~-k%i])