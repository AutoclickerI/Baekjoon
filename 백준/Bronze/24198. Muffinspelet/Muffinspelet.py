N=n=int(input())
a=0
while n:p=n//2;n=p//2;a+=p-n
print(a,N-a)