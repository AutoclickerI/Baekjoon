[N,K],s,*z=[*map(str.split,open(0))][::2]
K=int(K)
f=' '.join
l=[f(s[i:i+K])for i in range(len(s)-K+1)]
for s in z:s+='_';*l,=filter(f(s+s[::-1]).__contains__,l)
print('YNEOS'[l==[]::2])