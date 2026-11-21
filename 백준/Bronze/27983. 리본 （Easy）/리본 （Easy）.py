I=lambda:map(int,input().split())
n=int(input())
l=[*zip(I(),I(),input().split(),range(1,n+1))]
for i in range(n):
 for j in range(i+1,n):p,q=l[i],l[j];(q[0]-p[0]<=q[1]+p[1]and p[2]!=q[2])and exit(print(f'YES\n{p[3]}',q[3]))
print('NO')