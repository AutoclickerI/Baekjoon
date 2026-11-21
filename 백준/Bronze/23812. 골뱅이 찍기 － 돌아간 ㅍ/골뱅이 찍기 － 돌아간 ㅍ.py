n=int(input())
s='@'*n
l=[s+'   '*n+s]*n+[s*5]*n
print(*l*2+l[:n])