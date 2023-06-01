n=int(input())
l=[[i,0]for i in map(int,input().split())]
*L,=l
L.sort()
for i in range(n):L[i][1]=i
for i,j in l:print(j)