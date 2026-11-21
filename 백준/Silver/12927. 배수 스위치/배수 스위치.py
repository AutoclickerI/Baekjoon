*l,=map('Y'.__eq__,input())
r=0
for i in range(len(l)):
    if l[i]:
        r+=1
        for j in range(i,len(l),i+1):l[j]^=1
print(r)