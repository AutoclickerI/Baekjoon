import re
print(re.sub(r'([^aeiouy ])\1+',r'\1\1',input()))