n=int(input())
b=eval('input(),'*n)
s=''.join(b).count('C')//2
a=eval('n*[1],'*n)
i=0
while s:
    y,x=i//n,i%n
    s-=b[y][x]=='C'
    a[y][x]=2
    i+=1
for i in a:print(*i,sep='')