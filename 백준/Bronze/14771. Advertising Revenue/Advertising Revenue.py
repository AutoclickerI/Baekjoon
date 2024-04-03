for i in range(int(input())):
    n,v=map(int,input().split())
    ans=0
    ads=[[*map(int,input().split())]for _ in[0]*n]
    for _ in[0]*v:p,q,r=map(int,input().split());ans+=ads[p-1][1]*(ads[p-1][0]==1or r==1)+ads[q-1][1]*(ads[q-1][0]==1or 1<r)
    print(f'Data Set {i+1}:\n{ans}\n')