n=int(input())
l=['@'*n+' '*3*n+'@'*n]*n+['@'*5*n]*n
print(*(l*3)[:5*n])