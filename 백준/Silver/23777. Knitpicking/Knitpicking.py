import sys

input=sys.stdin.readline
#sys.setrecursionlimit(2*10**5)

N=int(input())
d={}
for _ in[0]*N:
    name,type,cnt=input().split()
    d[name]=d.get(name,{})
    d[name][type]=d[name].get(type,0)+int(cnt)

f=0

for name in d:
    for i in d[name]:
        if i=='any'and d[name][i]>1:
            f=1
        if 1<len(d[name]):
            f=1

if f:
    worst_cnt=0
    for name in d:
        l=[d[name].get('left',0),d[name].get('right',0),min(d[name].get('any',0),1)]
        worst_cnt+=max(l)
    print(worst_cnt+1)
else:
    print('impossible')