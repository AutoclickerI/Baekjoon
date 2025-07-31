s=c=0
for i in[*open(0)][1][::2]:
 p=(c!=i or p)*2;s+=p;c=i
 if 99<s:s=c=0
print(s)