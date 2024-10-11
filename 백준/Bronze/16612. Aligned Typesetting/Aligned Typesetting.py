n,L=map(int,input().split())
for _ in range(n):L-=len(input())
if n==1:print('No'if L else'Yes')
else:print('No'if L<n-1 or L%(n-1) else'Yes')