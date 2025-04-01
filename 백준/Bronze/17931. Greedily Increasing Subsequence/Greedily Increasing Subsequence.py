l=[0]
for i in map(int,[*open(0)][1].split()):
    if l[-1]<i:l+=i,
print(len(l)-1)
print(*l[1:])