f=open(0)
a=bytearray(1<<22)
s=""
while c:=f.read(1):
 s+=c
 if'0'>c:n=int(s);r=1<<n%8;r&a[n>>3]or print(n);a[n>>3]|=r;s=c