N,M=map(int,input().split())
*l,=map(int,input().split())

s=0
e=10**10

while 1<e-s:
    m=(s+e)//2
    if M<=sum(max(i-m,0)for i in l):
        s=m
    else:
        e=m
print(s)