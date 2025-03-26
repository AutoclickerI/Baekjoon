def dfs(s):
    if s in v:
        return
    v.add(s)
    for e in d.get(s,[]):
        dfs(e)
    a.append(s)

for T in range(1,int(input())+1):
    d={}
    for _ in[0]*int(input()):
        s,e=input().split(':')
        d[s]=d.get(s,[])
        d[s]+=e,
    v=set()
    a=[]
    for _ in[0]*int(input()):
        dfs(input())
    
    print(f'Case #{T}:',len(a))
    for i in a:
        print(i)