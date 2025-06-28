import re
l=[re.findall('...',f'{ord(i):b}'.translate({49:42,48:46}))for i in'篭篯礧筯秧']
input()
for i in zip(*[l[ord(i)-65]for i in input()]):print(*i,sep='')