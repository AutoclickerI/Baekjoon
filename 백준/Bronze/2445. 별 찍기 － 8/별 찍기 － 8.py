n=int(input())
[print('*'*i+' '*2*(n-i)+'*'*i)for i in range(1,n)];[print('*'*i+' '*2*(n-i)+'*'*i)for i in range(n,0,-1)]