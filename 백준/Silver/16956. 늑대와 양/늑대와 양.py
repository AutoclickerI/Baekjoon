R,C=map(int,input().split())
l=[input()for _ in[0]*R]
f=0
for i in*l,*zip(*l):f|=any(v in''.join(i)for v in('SW','WS'))
print(1-f)
if f<1:
    for i in l:print(i.replace(*'.D'))