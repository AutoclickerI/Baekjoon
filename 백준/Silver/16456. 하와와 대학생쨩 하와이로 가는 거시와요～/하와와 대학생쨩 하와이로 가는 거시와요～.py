a=b=c=1
for _ in[0]*int(input()):a,b,c=b,c,a+c;c%=10**9+9
print(a)