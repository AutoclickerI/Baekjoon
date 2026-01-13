c=3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1

l=[]
for i,j in zip(*open(0)):l+=i,j
l=[c[ord(i)-65]for i in l[:-2]]
while l[2:]:l=[(i+j)%10 for i,j in zip(l,l[1:])]
print(*l,sep='')