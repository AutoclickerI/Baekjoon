import re
s=input()
print('invalid'*('/0'in s)or'%o'%eval(re.sub('(\d+)(/?)',r'0o\1\2\2',s)))