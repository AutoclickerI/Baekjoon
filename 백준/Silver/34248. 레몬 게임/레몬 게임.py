s=[]
for c in[*open(0)][1][::2]:
    if c=='2':
        if s and s[-1]=='1':
            s.pop()
        else:
            s+=c
    else:
        if s and s[-1]=='2':
            s.pop()
        else:
            s+=c
while 2<len(s):
    p,q,r=s.pop(),s.pop(),s.pop()
    if p==q==r=='1':
        continue
    else:
        s=[1]
        break
if s:
    print('No')
else:
    print('Yes')