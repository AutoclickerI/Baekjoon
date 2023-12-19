N,M=map(int,input().split())
b=[[*input()]for _ in[0]*3*N]
for i in range(1,3*N,3):
    for k in range(M):
        eval1=eval(''.join(b[i][1+8*k:7+8*k]).strip('.').replace('=','=='))
        if eval1:
            f=b[i][6+8*k]!='.'
            b[i][0+8*k]='*'
            b[i][6+f+8*k]='*'
            for j in range(1+8*k,6+8*k+f):
                b[i-1][j]=b[i+1][j]='*'
        else:
            b[i][2+8*k]=b[i+1][1+8*k]=b[i-1][3+8*k]='/'
for i in b:
    print(''.join(i))