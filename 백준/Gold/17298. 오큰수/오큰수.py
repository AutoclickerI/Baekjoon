s,*r=[-1],
for i in map(int,[*open(0)][1].split()[::-1]):
 while 0<s[-1]<=i:s.pop()
 r+=s[-1],;s+=i,
print(*r[::-1])