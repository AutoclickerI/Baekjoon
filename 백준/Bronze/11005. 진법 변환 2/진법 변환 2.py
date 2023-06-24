p,q=map(int,input().split())
i=0
a=''
while q**i<=p:i+=1
for _ in[0]*i:
    i-=1
    n=p//q**i
    a+=chr(48+n+7*(n>9))
    p-=q**i*n
print(a)