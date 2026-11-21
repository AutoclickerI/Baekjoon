a=b=c=0
m=10**9+7
for i in[*open(0)][1].split():i=int(i);a+=1//i;c+=i//3*b;b+=~i%2*(a+b);b%=m
print(c%m)