N,_,P=map(int,input().split())
l=[[*map(int,input().split())]for _ in[0]*N]
Q=[[*map(int,input().split())]for _ in[0]*P]
print(sum(all(i[j-1]==k for j,k in Q)for i in l))