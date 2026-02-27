s=input()
r=0
for i in range(1,len(s)+1):
    r+=s[max(i-2,0):i]=='ha'
    r-=s[max(i-5,0):i]=='boooo'
    r+=3*(s[max(i-5,0):i]=='bravo')
print(r)