n=int(input())
s=['@'*n+'   '*n+'@'*n]*n
k=['@'*5*n]*n
print(*s*2+k+s+k)