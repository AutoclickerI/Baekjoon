l=[[*map(int,input().split())]for _ in[0]*8]
s=input()
if s=='D':l=l[::-1]
if s=='R':l=[[*i][::-1]for i in zip(*l)][::-1]
if s=='L':l=[[*i]for i in zip(*l)]
    
#U기준
for _ in range(8):
    for i in range(1,8):
        for j in range(8):
            if l[i-1][j]==0!=l[i][j]:l[i-1][j],l[i][j]=l[i][j],0
for i in range(1,8):
    for j in range(8):
        if l[i-1][j]==l[i][j]:l[i-1][j]*=2;l[i][j]=0
for _ in range(8):
    for i in range(1,8):
        for j in range(8):
            if l[i-1][j]==0!=l[i][j]:l[i-1][j],l[i][j]=l[i][j],0
if s=='D':l=l[::-1]
if s=='R':l=[[*i][::-1]for i in zip(*l)][::-1]
if s=='L':l=[[*i]for i in zip(*l)]
[print(*i)for i in l]