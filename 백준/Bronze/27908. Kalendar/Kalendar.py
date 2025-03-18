n,d=map(int,input().split())
l=['.']*~-d+[*range(1,n+1)]
l+=-len(l)%7*['.']
z='+---------------------+'
print(z)
for i in zip(*[iter(l)]*7):
    print(end='|')
    for j in i:print(end=('..'+str(j))[-3:])
    print('|')
print(z)