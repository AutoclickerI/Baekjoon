n=int(input())
a='* '*((1+n)//2)
b=' *'*(n//2)
for i in range(2*n):
    print(a if i%2==0 else b)
