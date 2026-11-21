H,W=map(int,input().split())
C,D=map(int,input().split())

try:
    i=H-1
    j=i-1
    l=[W*[1]for _ in[0]*H]
    for i in range(1,H):
        for j in range(i):
            l[i][j]=9
            D-=1
    
    j+=1
    assert 0<=D
    
    while D and 0<=i:
        while D and j<W-(H-1-i):
            l[i][j]=9
            D-=1
            j+=1
        i-=1
        j=i
    assert D==0
    for i in l:
        print(*i)
except:
    print(-1)