n=int(input())
l=['@'*5*n]*n
print(*l+['@'*n+' '*3*n+'@'*n]*3*n+l)