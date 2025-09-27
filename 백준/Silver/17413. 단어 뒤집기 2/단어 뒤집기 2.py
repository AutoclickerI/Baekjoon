import re
print(''.join(a+b[::-1]for a,b in re.findall('(<.*?>| )|([^<> ]+)',input())))