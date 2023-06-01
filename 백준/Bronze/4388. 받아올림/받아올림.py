for i in[*open(0)][:-1]:
 a,b=map(int,i.split());c=t=0
 while a+b:c=c+a%10+b%10>9;t+=c;a//=10;b//=10
 print(t)