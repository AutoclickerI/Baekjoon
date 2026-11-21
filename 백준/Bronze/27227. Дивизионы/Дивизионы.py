p,s=open(0)
p=int(p)
n=1+(p<1901)+(p<1601)
if str(n)in s:print(n)
else:
 for i in s[:-1]:print(str(i)+'*'*(int(i)>n))