_,s,*l=open(0)
a=len(s)
for t in l:
 i=0
 while s[:-1][:i]==t[:i]:i+=1
 a+=min(0,len(s)-2*i+2)+len(s:=t)
print(a-1)