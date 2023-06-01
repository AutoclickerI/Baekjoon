input()
d={}
for i in input().split():d[i]=d[i]+1if d.get(i)else 1
input()
for i in input().split():print(d.get(i)or 0)