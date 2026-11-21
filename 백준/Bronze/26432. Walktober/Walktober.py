for k in range(int(input())):
    p,q,r=map(int,input().split())
    l=[[*map(int,input().split())]for _ in[0]*p]
    tr=[[l[i][j]for i in range(len(l))]for j in range(len(l[0]))]
    print(f"Case #{k+1}:",sum(max(tr[i])-tr[i][r-1]for i in range(len(tr))))