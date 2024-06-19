N,M=map(int,input().split())
*s,=zip(*eval('map(int,input()),'*N))
l=[[0]*N]
for i in s:l+=[i[j]+max(l[-1][max(0,j-1):j+2])for j in range(N)],
print(max(l[-2]))