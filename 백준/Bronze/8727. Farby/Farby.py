x,y,z,a,b,c,d,e,f=map(int,open(0).read().split())
for i in e-x+(d+f)/2,a-y+(b+f)/2,c-z+(b+d)/2:i=max(0,i);print(i%1and'%.1f'%i or int(i))