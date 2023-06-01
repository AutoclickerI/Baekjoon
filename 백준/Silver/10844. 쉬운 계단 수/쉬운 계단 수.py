a=[0]+[1]*9
for i in range(1,int(input())):
    b=a.copy()
    b[0]=a[1]
    b[9]=a[8]
    for j in range(1,9):
        b[j]=a[j-1]+a[j+1]
    a=b
print(sum(a)%10**9)