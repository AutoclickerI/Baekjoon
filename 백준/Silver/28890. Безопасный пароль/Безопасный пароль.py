s=input()
a=''
l=[0]*26
se={chr(i+97)for i in range(26)}
for idx,i in enumerate(s):
    if a[-2:]==i+i or l[ord(i)-97]>=len(s)//2:
        i=min(se-{i,*s[idx+1:idx+2]},key=lambda c:l[ord(c)-97])
    a+=i
    l[ord(i)-97]+=1
print(a)