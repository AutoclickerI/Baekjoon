s=input()
f=1
for i in range(len(s)):f&=s!=s[::-1];s=s[-1]+s[:-1]
print('yneos'[f::2])