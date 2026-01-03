import sys
input=sys.stdin.readline

for T in[0]*int(input()):
    n,k,t,m=map(int,input().split())
    d=[{'cnt':0}for _ in[0]*n]
    for v in range(m):
        i,j,s=map(int,input().split())
        i-=1
        d[i]['last']=v
        d[i]['cnt']+=1
        d[i][j]=max(d[i].get(j,0),s)
    dt=d[t-1]
    d.sort(key=lambda i:(-sum(i[j]for j in i if type(j)==int),i['cnt'],i['last']))
    print(d.index(dt)+1)