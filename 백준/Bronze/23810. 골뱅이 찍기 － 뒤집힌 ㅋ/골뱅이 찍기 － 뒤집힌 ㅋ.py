n=int(input())
s='@'*n
l=[s*5]*n+[s]*n
print(*l*2+l[-n:])