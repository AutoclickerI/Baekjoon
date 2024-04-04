for _ in[0]*int(input()):
    input()
    n,e=map(int,input().split())
    *l,=range(n+1)
    m=0
    for i in[int(input())for _ in[0]*e][::-1]:
        if l[i]:m=i;l[i]=0
    for i in l:
        if l[i]:m=i
    print(m)