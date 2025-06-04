import re
a,b=map(re.match,['.*?[aeiou]+(?=[^aeiou\n])']*2,open(0))
print(a and b and a.group()+b.group()or'no such exercise')