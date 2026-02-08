l=[0]
for i in map(int,[*open(0)][1].split()[::-1]):
    l+=min(l[-1]+1,i),
print(sum(l))