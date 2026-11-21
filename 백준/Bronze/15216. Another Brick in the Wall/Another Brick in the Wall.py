h,w,n=map(int,input().split())
l=[w]*h
for i in map(int,input().split()):
    if l[-1]==0:l.pop()
    if not l:
        exit(print('YES'))
    l[-1]-=i
if l[-1]==0:l.pop()
if not l:
    print('YES')
else:
    print('NO')