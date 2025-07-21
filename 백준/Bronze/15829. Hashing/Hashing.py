for c in[*open(v:=0,'rb')][1][-2::-1]:v=c%32+31*v
print(v%1234567891)