n=int(input())
l=[]
while n:
    l+=n%256,
    n//=256
for i in l:
    n*=256
    n+=i
print(n)