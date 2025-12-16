s=[]
c=0
for i in*[*map(int,open(0).read().split())][2::2],0:
    while s and i<=s[-1]:
        c+=s.pop()!=i
    s+=i,
print(c)