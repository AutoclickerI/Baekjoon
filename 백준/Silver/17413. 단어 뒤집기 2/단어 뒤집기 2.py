import re
for a,b in re.findall('(<.*?>)|([^<> ]+| )',input()):print(end=a+b[::-1])