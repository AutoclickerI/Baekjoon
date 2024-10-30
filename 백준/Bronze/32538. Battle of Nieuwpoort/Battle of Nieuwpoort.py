def t_n(n,b):
    s=''
    while n:
        s+='0123456789abcdef'[n%b]
        n//=b
    return s[::-1]
s=['impossible']
n=int(input().split()[0])
for i in range(2,17):
    if n%i**2<1:s=i,t_n(n,i)
print(*s)