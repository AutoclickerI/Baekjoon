for _ in range(int(input())):
    input()
    r,c=map(int,input().split())
    a=[input().replace(' ','')for _ in range(r)]
    ans=0
    for i in range(r):
        for j in range(c):
            if j+2<c and a[i][j]==a[i][j+1]==a[i][j+2]:ans=(i+1,j+1,i+1,j+2,i+1,j+3);break
            elif i+2<r and a[i][j]==a[i+1][j]==a[i+2][j]:ans=(i+1,j+1,i+2,j+1,i+3,j+1);break
    print(*ans or['no set found'])