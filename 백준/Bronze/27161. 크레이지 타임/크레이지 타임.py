t=b=1
for i in[*open(0)][1:]:p=i[0]=='H';q=int(i[-3:])==t;x=p^q;b^=p*x;print(t,'NYOE S'[q*x::2]);t=(t+2*b-2)%12+1