n=int(input())
input()
f=0
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        f=1
print('No'if f else 'Yes')