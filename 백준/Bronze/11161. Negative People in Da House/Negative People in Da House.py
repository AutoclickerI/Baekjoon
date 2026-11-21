I=input
for _ in[0]*int(I()):
 m=p=0
 for _ in[0]*int(I()):a,b=map(int,I().split());p+=b-a;m=max(m,p)
 print(m)