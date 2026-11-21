i=iter(open(0))
input=lambda:next(i)
for _ in[0]*int(input()):
 N=int(input());a=n=0
 for _ in[0]*N:n+=int(input());a+=n<0;n+=n<0
 print(abs(n)+a)