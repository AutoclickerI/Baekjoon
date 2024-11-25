N,M=map(int,input().split())
arr1=[[*map(int,input().split())]for _ in[0]*N]
arr2=[[*map(int,input().split())]for _ in[0]*N]
arr=[[abs(k-l)for k,l in zip(i,j)]for i,j in zip(arr1,arr2)]
m=0,*map(max,zip(*arr))
print(sum(m[i]for i in map(int,input().split())))