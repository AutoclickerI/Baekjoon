n=int(input())
a='* '*n
for i in range(n):
    print(a if i%2==0 else ' '+a)