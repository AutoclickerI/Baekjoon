import re
s=input()
for _ in[0]*99:s=re.sub(r"('\w)|(\w')",'',s)
print(re.sub(' ','',s))