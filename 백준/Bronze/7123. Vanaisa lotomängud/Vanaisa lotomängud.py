l=[]
for _ in[0]*int(input()):
    l+=-eval(input().replace(*' -')),
if sum(l)>0:
    print('PLUSSIS')
elif sum(l)==0:
    print('NULLIS')
else:
    print('MIINUSES')
if min(l)<0:
    print(l.index(min(l))+1,-min(l))
else:
    print(0,0)
m=1
ans=(0,0,0)
for i in range(len(l)):
    for j in range(i,len(l)):
        if sum(l[i:j+1])<m:
            m=sum(l[i:j+1])
            ans=(i+1,j+1,-sum(l[i:j+1]))
print(*ans)