s=input()
d=[1]+[0]*len(s)
for i in range(len(s)):
    if s[i:i+1]!='0':
        d[i+1]+=d[i]
    if 9<int(s[max(i-1,0):i+1])<35:
        d[i+1]+=d[i-1]
print(d[-1])