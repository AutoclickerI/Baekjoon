for i in[*open(0,'rb')][1:]:
 t=[0]*99;p=f=0
 for c in i:f|=0<p!=c;t[c]+=p<1;p=(t[c]%3<1>p)*c
 print(f*'FAKE'or'OK')