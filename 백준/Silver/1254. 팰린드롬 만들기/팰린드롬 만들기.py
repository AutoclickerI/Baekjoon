i=len(s:=input())
while s!=s[::-1]:_,*s=s;i+=1
print(i)