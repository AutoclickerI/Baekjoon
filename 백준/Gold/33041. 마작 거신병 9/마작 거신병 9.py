H=int(input())
*W,=map(int,input().split())
C,D=map(int,input().split())

l=[[i,0,i*[1]]for i in W]

try:
    i=H-1
    for i in range(1,H):
        while l[i][0]<=l[i-1][0]:
            l[i][2][l[i][1]]=9
            l[i][0]+=8
            l[i][1]+=1
            D-=1
    assert 0<=D
    while D and l[i][1]<W[i]:
        l[i][2][l[i][1]]=9
        l[i][0]+=8
        l[i][1]+=1
        D-=1
    i-=1
    while D and 0<=i:
        while D and l[i][1]<W[i] and l[i][0]+8<l[i+1][0]:
            l[i][2][l[i][1]]=9
            l[i][0]+=8
            l[i][1]+=1
            D-=1
        i-=1
    assert D==0
    for _,_,i in l:print(*i)
except:
    print(-1)