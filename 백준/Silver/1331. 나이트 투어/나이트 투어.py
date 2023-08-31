l=[0]*36
s,e=a,b=input()
l[(ord(a)-65)*6+ord(b)-49]=1
for _ in l[1:]:
    c,d=input()
    l[(ord(c)-65)*6+ord(d)-49]=1
    if(ord(a)-ord(c))**2+(ord(b)-ord(d))**2!=5:exit(print('Invalid'))
    a,b=c,d
print(['Inv','V'][all(l)and((ord(s)-ord(a))**2+(ord(e)-ord(b))**2==5)]+'alid')