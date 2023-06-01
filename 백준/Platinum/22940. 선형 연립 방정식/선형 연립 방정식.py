from fractions import*
n=[list(map(int,input().split()))for i in[0]*int(input())]
def gauss(x):
    for i in range(len(x)):
        x[i]=[x[i][j]/x[i][i]for j in range(len(x[0]))]
        for j in range(i+1,len(x)):
            while 1:
                try:
                    x[j]=[x[j][k]-x[i][k]*(x[j][i]/x[i][i])for k in range(len(x[0]))]
                    break
                except:
                    cache=x[i]
                    del x[i]
                    x+=[cache]
    for i in range(len(x)-1,0,-1):
        x[i]=[x[i][j]/x[i][i]for j in range(len(x[0]))]
        for j in range(i-1,-1,-1):
            while 1:
                try:
                    x[j]=[x[j][k]-x[i][k]*(x[j][i]/x[i][i])for k in range(len(x[0]))]
                    break
                except:
                    cache=x[i]
                    del x[i]
                    x+=[cache]
    return x
ans=[round(i[-1])for i in gauss(n)]
print(*ans)