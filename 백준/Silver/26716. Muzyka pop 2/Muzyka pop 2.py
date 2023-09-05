n=int(input())
l=[]
i=0
while n>0:
    i+=1
    l+=i,
    n-=i.bit_count()
l=l[::-1]
for i in range(len(l)):
    if n+l[i].bit_count()==0:
        l.pop(i)
        break
print(len(l))
print(*l)