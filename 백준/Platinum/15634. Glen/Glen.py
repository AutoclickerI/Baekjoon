N,M=map(int,input().split())
l=[list(input())for i in[0]*N]
s=''
for i in range(N):
    if i%2==0:
        s+='R'*(M-1)
    else:
        s+='L'*(M-1)
    if i!=N-1:
        s+='D'
s+='L'if N%2==0 else'R'
print('R',end='')
dic={'R':'L','L':'R','D':'U'}
for i in range(N):
    if i%2==0:
        for j in range(M):
            if l[i][j]=='.':
                try:
                    l[i][j+1]='#'if l[i][j+1]=='.' else'.'
                except:
                    if i!=N-1:
                        l[i+1][j]='#'if l[i+1][j]=='.' else'.'
                print(s[i*M+j]+dic[s[i*M+j]],end='')
            if i*M+j<len(s)-1:
                print(s[i*M+j],end='')
    else:
        for j in range(M-1,-1,-1):
            if l[i][j]=='.':
                try:
                    if j==0:raise
                    l[i][j-1]='#'if l[i][j-1]=='.' else'.'
                except:
                    if i!=N-1:
                        l[i+1][j]='#'if l[i+1][j]=='.' else'.'
                print(s[i*M+M-1-j]+dic[s[i*M+M-1-j]],end='')
            if i*M+M-1-j<len(s)-1:
                print(s[i*M+M-1-j],end='')