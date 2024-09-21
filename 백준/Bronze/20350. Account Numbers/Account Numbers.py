s=input()
s=s[4:]+s[:4]
for i in range(65,91):s=s.replace(chr(i),str(i-55))
print('in'*(int(s)%97!=1)+'correct')