import re
input()
print(re.sub(r'[aeiouy](?=[^aeiouy ]{2,})','',input())[::-1])