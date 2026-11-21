i,s=open(0,'rb')
_,a,b=map(int,i.split())
for i in s:print(end=chr(32+i//65*((i+13-a**b)%26+33)))