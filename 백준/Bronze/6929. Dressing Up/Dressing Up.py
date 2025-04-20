n=int(input())
for i in range(1,n,2):print('*'*i+' '*(n-i)*2+'*'*i)
print('**'*n)
for i in range(n-2,0,-2):print('*'*i+' '*(n-i)*2+'*'*i)