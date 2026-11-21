n=int(input())
s=['@'*5*n]*n
print(*s+['@'*n]*n*3+s)