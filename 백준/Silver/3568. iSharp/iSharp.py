import re
b,*l=input().split()
for i in l:t,*s=re.findall('\[\]|\&|\*|\w+',i);print(b,*s[::-1],' ',t,';',sep='')