import re
n,l=open(0)
print(*[int(n)*int(i)for i in re.findall('\d+',l)]or['N/A'])