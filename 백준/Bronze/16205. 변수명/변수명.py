import re
s=re.findall('[^_][a-z]*',input().split()[1])
*a,=map(str.capitalize,s)
z=''.join(a)
print(z[0].lower()+z[1:],'_'.join(a).lower(),z)