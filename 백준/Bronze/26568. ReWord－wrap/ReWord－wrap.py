for T in range(int(input())):
    if T:print()
    N=int(input())
    l=[]
    for _ in[0]*int(input()):
        l+=input().split(' ')
    s=[l[0]]
    for i in l[1:]:
        if len(s[-1]+' '+i)<=N:
            s[-1]+=' '+i
        else:
            s+=i,
    for i in s:print(i)