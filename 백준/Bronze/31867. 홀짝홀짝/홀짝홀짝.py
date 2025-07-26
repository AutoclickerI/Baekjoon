for i in[*open(c:=0,'rb')][1]:c+=i%-2|1
print((c<1)-(c==1))