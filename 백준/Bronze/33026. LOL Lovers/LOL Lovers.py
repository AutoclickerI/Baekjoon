input()
s=input()
L=s.count('L')
O=s.count('O')
for i in range(1,len(s)):
    if s[:i].count('L')*2!=L and s[:i].count('O')*2!=O:exit(print(i))
print(-1)