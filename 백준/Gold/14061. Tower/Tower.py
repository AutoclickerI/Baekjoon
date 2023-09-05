h=int(input().split()[1])
c=[]
m=0
for i in map(int,input().split()):
    if i>h:c=[];continue
    while c and c[-1]<i:c.pop()
    c+=i,
    m=max(m,len(c))
print(m)