a=1;b=c=0
for i in[0]*int(input()):b=a+b;a,c=(b*2+c)%(10**9+7),a
print(a)