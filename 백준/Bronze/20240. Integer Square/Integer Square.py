N=int(input())

x=0
for i in range(100):
    for j in range(100):
        if i*i+j*j==N:x=i,j

if x:
    i,j=x
    print(0,0)
    print(i,j)
    print(-j,i)
    print(i-j,i+j)
else:
    print('Impossible')