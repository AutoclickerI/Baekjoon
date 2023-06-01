b,n,k=[0,31,28,31,30,31,30,31,31,30,31,30,31],0,list(map(int, input().split()))
for i in range(k[0]):n+=b[i]
p=(n+k[1])%7*3;print('SUNMONTUEWEDTHUFRISAT'[p:p+3])