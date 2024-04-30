t=1000
for s in[*open(0,'rb')][1:]:k=sum(s)-634+int(s)%t*10;print(str(k+t*(k<t))[-4:])