input()
l=input().split()
p='0'
q=0
d={'0':'1','1':'2','2':'0'}
for i in range(len(l)):
    if p==l[i]:
        q+=1
        p=d[p]
print(q)