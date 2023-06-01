n=int(input())
p,q=map(int,input().split())
for _ in[0]*n:
    a,b,c,d=map(int,input().split())
    if a<=p<=c and b<=q<=d:exit(print('Yes'))
print('No')