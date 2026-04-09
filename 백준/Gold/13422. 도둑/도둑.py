for _ in[0]*int(input()):
    N,M,K=map(int,input().split())
    l=[*map(int,input().split())]*2
    s=sum(l[:M])
    if N==M:
        print(+(s<K))
        continue
    r=0
    for i in range(N):
        s+=l[i+M]-l[i]
        r+=s<K
    print(r)