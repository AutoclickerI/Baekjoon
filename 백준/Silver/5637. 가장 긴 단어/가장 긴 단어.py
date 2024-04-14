import re
print(max(re.findall('[a-z-]+',open(0).read().lower()),key=len))