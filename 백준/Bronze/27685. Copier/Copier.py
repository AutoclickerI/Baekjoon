for _ in[0]*int(input()):
    input()
    input()
    *l,=map(int,input().split())
    s=set()
    ans=[]
    for i in l:
        if i not in s:
            ans+=i,
            s.add(i)
    print(*ans)