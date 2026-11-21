n=int(input())
a,b=['@'*5*n]*n,['@'*n]*n
print(*(a+b)*2+a)