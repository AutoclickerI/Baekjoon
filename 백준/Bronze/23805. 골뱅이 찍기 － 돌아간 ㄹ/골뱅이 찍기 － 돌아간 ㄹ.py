n=int(input())
s=' '*n+'@'*n
l=['@'*3*n+s]
print(*l*n+['@'*n+s*2]*3*n+[l[0][::-1]]*n)