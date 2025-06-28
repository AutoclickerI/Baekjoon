for l in[*open(0)][1:]:
 i=t=int(l);print(t)
 while t>=100:x=t%10;t//=10;t-=x;print(t)
 print('The number',i,'is'+' not'*(0<t%11),'divisible by 11.\n')