for _ in[0]*int(input()):
    l=input().split()
    s=set()
    while(i:=input())!='what does the fox say?':
        s.add(i.split()[-1])
    print(*[i for i in l if i not in s])