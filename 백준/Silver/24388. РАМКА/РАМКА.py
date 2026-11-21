a,b,k=map(int,input().split())
x=a%k+b%k
print(a//k*2+b//k*2+(x>0)+(x>k/2)+(x>k)+(min(a%k,b%k)>k/2))