L,W,H=map(int,input().split())
N=int(input())

cnt=[0]*20
for _ in[0]*N:
    a,b=map(int,input().split())
    cnt[a]=b

fw=0
r=0

for i in range(19,-1,-1):
    fw<<=3
    use=min(cnt[i],(L>>i)*(W>>i)*(H>>i)-fw)
    fw+=use
    r+=use

print(-(fw<L*W*H)or r)