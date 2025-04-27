import re
_,s,*l=open(0)
for i in l:print(re.match(s.replace('*','.*'),i)and'DA'or'NE')