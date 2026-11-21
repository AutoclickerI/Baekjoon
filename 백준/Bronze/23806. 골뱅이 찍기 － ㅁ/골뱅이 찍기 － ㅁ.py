n=int(input())
s='@'*n
l=[s*5]*n
print(*l+[s+' '*3*n+s]*3*n+l)