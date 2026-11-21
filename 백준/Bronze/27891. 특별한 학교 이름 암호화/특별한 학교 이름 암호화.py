d={'northlondo':'NLCS','branksomeh':'BHA','koreainter':'KIS','stjohnsbur':'SJA'}
s=[*input()]
while 1:
    if ''.join(s)in d:break
    for j in range(10):
        s[j]=chr((ord(s[j])+1)-(s[j]>'y')*26)
print(d[''.join(s)])