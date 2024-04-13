import re
print(*sorted(map(int,re.findall('\d+',open(0).read())[1:])))