# end with 0 / end with 1
v=[[2*[0]for _ in[0]*101]]
v[0][0][0]=1
for _ in[0]*100:
    p=v[-1]
    t=[2*[0]for _ in[0]*101]
    t[0]=p[0][0]+p[0][1],p[0][0]
    for i in range(1,101):
        t[i][0]=p[i][0]+p[i][1]
        t[i][1]=p[i][0]+p[i-1][1]
    v+=t,

for i in[*open(0)][1:]:
    n,k=map(int,i.split())
    print(sum(v[n][k]))