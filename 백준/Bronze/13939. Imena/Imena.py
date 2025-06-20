import re
print(*[len(re.findall(r'\b[A-Z][a-z]*\b',s))for s in re.split('[.?!]',[*open(0)][1][:-1])if s])