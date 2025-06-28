for i in[*open(0)][1:]:
 i=t=int(i)
 while 99<t:print(t);t=t//10-t%10
 print(t,'The number',i,'is'+' not'*(0<t%11),'divisible by 11.\n')