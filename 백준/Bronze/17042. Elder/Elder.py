s,_,*q=open(0)
S={s:=s[0]}
for i in q:
 a,b=i.split()
 if b==s:s=a;S.add(s)
print(s,len(S))