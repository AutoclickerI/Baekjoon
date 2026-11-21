d={}
c={}
for i in[*open(0)][1:]:
    p,q=i.split()
    d[p]=d.get(p,0)+int(q)
    c[p]=c.get(p,0)+1
M=c.get('M',0)and d['M']/c['M']
J=c.get('J',0)and d['J']/c['J']
if M>J:print('M')
elif M<J:print('J')
else:print('V')