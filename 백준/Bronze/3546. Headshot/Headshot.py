n=len(s:=input())
x=y=0
s*=2
for i in range(n):
 if s[i]=='0':x+=(b:=s[i+1]=='0');y+=b^1
x,y=x*n,(x+y)**2
print(['ERQOUTAALT E'[x<y::2],'SHOOT'][x>y])