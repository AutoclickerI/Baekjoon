import re
for i in[*open(0)][1:]:print(re.sub(r'\b\w{4}\b','*'*4,i))