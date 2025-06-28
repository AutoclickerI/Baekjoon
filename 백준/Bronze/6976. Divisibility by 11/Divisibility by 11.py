for i in[*open(0)][1:]:
 i=t=int(i);
 while 100<=t:print(t);x=t%10;t//=10;t-=x
 print(t,'The number',i,'is'+' not'*(0<t%11),'divisible by 11.\n')