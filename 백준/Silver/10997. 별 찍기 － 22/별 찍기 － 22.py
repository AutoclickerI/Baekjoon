a=['*****','*    ','* ***','* * *','* * *','*   *','*****']
n=int(input())
for i in range(2,n):
    b=['*'*(4*i+1),'*'+' '*4*i,'* '+a[0]+'**']
    for j in range(1,len(a)):
        b.append('* '+a[j]+' *')
    b+=['*'+' '*(4*i-1)+'*','*'*(4*i+1)]
    a=b
if n==1:print("*")
else:
    for j in a:
        n=len(j)
        while j[n-1]==' ':
            n-=1
        print(j[:n])