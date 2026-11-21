import sys
input=sys.stdin.readline
l=[0]*1001
for _ in[0]*int(input()):
    p,q=input().split()
    if p=='jinju':
        price=int(q)
    else:
        l[min(int(q),1001)-1]+=1
print(price)
p=0
for i in range(price,1001):p+=l[i]
print(p)