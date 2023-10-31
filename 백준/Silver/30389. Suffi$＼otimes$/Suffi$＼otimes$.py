d={}
for _ in[0]*int(input()):
    n=len(s:=input())
    for i in range(n):
        d[s[i:]]=1-d.get(s[i:],0)
print(sum(d.values()))