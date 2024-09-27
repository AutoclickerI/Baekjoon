(N,M,H),*l=[[*map(int,i.split())]for i in open(0)]
while len(l)<N:l+=[],
a=0
for i in range(N):
    for j in range(len(l[i])):
        if l[i][j]>=H:
            a+=1
            continue
        if all(l[k][j]<H for k in range(i))or all(l[k][j]<H for k in range(i+1,N))or all(l[i][k]<H for k in range(j))or all(l[i][k]<H for k in range(j+1,len(l[i]))):
            continue
        a+=1
print(a)