for _ in[0]*int(input()):
    n=int(input())
    nl=[list(map(int,input().split())) for i in range(n)]
    s=int(input())
    for j in nl:rh=j.pop();fc,sc=sum(j),sum(j[rh:]);n-=((rh<0<s!=fc)or s%sc!=fc%sc)
    print(n)