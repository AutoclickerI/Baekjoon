s=a=0
for i in map(int,[*open(0)][1].split()):a=max(i-s,a);s+=i
print(a)