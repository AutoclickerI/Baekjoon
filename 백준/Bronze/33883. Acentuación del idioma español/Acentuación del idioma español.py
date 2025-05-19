s=input()
l=[]
for x in range(len(s)):
    if s[x]in'aeiou':l+=x+1,
try:
    if s[-1]in'aeiouns':print(l[-2])
    else:print(l[-1])
except:print(-1)