i=a=1
n=int(input())
while i<n:a=a*i%(10**9+7);i+=2
print(a)