_,s,*l=open(0)
a=len(s)
for t in l:
 m,k=len(s)-1,len(t)-1;i=0
 while m>i<k!=s[i]==t[i]:i+=1
 a+=k+min(1,2+m-2*i);s=t
print(a-1)