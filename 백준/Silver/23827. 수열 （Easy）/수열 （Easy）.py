a=p=0
for x in[*open(0)][1].split():x=int(x);a+=p*x;p+=x
print(a%(10**9+7))