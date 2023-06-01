l=[]
for i in range(1,999):
    for j in range(i):
        l+=[i]
a,b=map(int,input().split())
print(sum(l[a-1:b]))