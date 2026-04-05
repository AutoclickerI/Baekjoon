q=T=P=1
m=10**9+7
for i in range(1,n:=int(input())+1):p=pow(i,-1,m);q=2*(T+P*p)*p%m;P=(2*T+(i+4+2*p)*P)*p%m;T+=q
print((q-n*n)%m)