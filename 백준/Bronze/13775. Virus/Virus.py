n,a=open(0)
s=''
n=int(n)
for i in a:
 x=ord(i)
 if 96<x<123:s+=chr((x-n+7)%26+97);n=n%25+1
 else:s+=i
print(s)