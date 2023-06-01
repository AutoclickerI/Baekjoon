s=['*   ','**  ','* * ','****']
n=int(input())
for j in range(n-2):
    s=[i+' '*(4*2**j) for i in s]+[i*2 for i in s]
if n>1:
    for i in reversed(s):
        n=len(i)
        while i[n-1]==' ':
            n-=1
        print(i[:n])
else:
    print('*'if n==0 else '**\n*')
