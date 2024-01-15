s=open(0,'rb').read().upper()
*l,=map(s.count,range(65,91))
s=['ABCDEFGHIJKLMNOPQRSTUVWXYZ','-'*26]
while any(l):
    tmp=''
    for i in range(26):
        if l[i]:
            l[i]-=1
            tmp+=chr(i+65)
        else:
            tmp+=' '
    s+=tmp,
[print(i)for i in s[::-1]]