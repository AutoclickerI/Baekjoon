N,M=map(int,input().split())
db=[[*map(int,input().split())]for _ in[0]*N]
for _ in[0]*int(input()):
    *l,=map(int,input().split())
    print(sum(all(l[i]==j[i]for i in range(M)if l[i]!=-1)for j in db))