L,H,P,E,n=map(int,input().split())
l=[[0,0]for _ in[0]*4]
Lab=0
Hw=1
Proj=2
Exam=3
for _ in[0]*n:
    a,b,c,d=map(eval,input().replace(*'/ ').replace(*': ').split())
    l[a][0]+=c
    l[a][1]+=d
print(int(L*l[0][0]/l[0][1]+H*l[1][0]/l[1][1]+P*l[2][0]/l[2][1]+E*l[3][0]/l[3][1]))