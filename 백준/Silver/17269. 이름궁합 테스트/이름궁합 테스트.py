p,q=[*open(0)][1].split()
s=''.join(i+j for i,j in zip(p+' '*99,q+' '*99)).replace(' ','')
p=3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1
s=[p[ord(i)-65]for i in s]
while 2<len(s):s=[(i+j)%10 for i,j in zip(s,s[1:])]
print(10*s[0]+s[1],end='%')