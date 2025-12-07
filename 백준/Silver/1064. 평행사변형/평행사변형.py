a,b,c,d,e,f=map(int,input().split())
c-=a
e-=a
d-=b
f-=b
*x,=map(abs,[c+d*1j,e+f*1j,e-c+(f-d)*1j])
print(-(c*f==d*e)or(max(x)-min(x))*2)