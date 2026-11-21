i,*l=input()
a=b=c=i
v=w=x=0
for s in l:v+=a!=s;v+=s<'U';a='U';w+=b!=s;w+='D'<s;b='D';x+=c!=s;c=s
print(v,w,x)