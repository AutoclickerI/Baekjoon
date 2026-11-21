n=int(input())+1
*odd,=range(1,n,2)
odd.remove(7)
odd+=7,

*even,=range(2,n,2)
even.remove(8)
even+=8,

odd+=even
odd*=2

for i in range(n-1):
    print(*odd[i:i+n-1])