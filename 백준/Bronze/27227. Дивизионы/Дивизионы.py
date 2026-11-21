p,s=open(0)
p=int(p)
if str(n:=1+(p<1901)+(p<1601))in s:print(n)
else:
 for i in s[:-1]:print(str(i)+'*'*(int(i)>n))