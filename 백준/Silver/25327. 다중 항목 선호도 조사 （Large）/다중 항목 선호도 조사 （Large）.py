import sys
input=sys.stdin.readline

s=[[4*[0]for _ in[0]*4]for _ in[0]*4]
N,M=map(int,input().split())
for _ in[0]*N:
    a,b,c=input().split()
    a='- kor eng math'.split().index(a)
    b='- apple pear orange'.split().index(b)
    c='- red blue green'.split().index(c)
    for i in 0,a:
        for j in 0,b:
            for k in 0,c:
                s[i][j][k]+=1
for _ in[0]*M:
    a,b,c=input().split()
    a='- kor eng math'.split().index(a)
    b='- apple pear orange'.split().index(b)
    c='- red blue green'.split().index(c)
    print(s[a][b][c])