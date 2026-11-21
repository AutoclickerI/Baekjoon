P,I=print,input
exec('''s=p=2100;e=2400
c=S=1
l=[]
while s<e-1:
 m=(s+e)//2;P('?',m)
 if int(I()):p+=(s-p)*S;s=m
 else:
  if S:
   if s in l:e=m;l+=[s]
   else:
    P('?',s)
    if I()=='0':S,e,s=0,s,p
    else:e=m;l+=[s]
  else:e=m
if S:
 if s in l:P('!',s)
 else:P('?',s);P('!',s-1+int(I()))
else:P('!',s)
'''*int(I()))