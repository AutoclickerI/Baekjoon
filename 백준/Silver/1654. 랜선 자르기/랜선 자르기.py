v,*o=open(0)
s=[0,2**31]
while s[1]-s[0]>1:l=sum(s)//2;s[sum(int(i)//l for i in o)<int(v.split()[1])]=l
print(s[0])