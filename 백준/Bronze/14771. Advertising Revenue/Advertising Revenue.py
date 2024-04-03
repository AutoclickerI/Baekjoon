I=lambda:map(int,input().split())
for i in range(*I()):
    n,v=I();ans=0;ads=[[*I()]for _ in[0]*n]
    for _ in[0]*v:p,q,r=I();ans+=ads[p-1][1]*(ads[p-1][0]or r==1)+ads[q-1][1]*(ads[q-1][0]or 1<r)
    print(f'Data Set {i+1}:\n{ans}\n')