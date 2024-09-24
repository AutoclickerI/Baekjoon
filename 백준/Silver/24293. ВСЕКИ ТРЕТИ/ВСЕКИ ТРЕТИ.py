*s,=input()
while 2<len(s):del s[2::3];s=s[::-1]
print(*sorted(s),sep='')