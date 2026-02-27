n=int(input())
s=n*~-n//2
t=''
for c in input():
 t+=c
 if'0'>c:s-=int(t);t=''
print(int(t)-s)