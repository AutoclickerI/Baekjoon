n=int(input())
k,m1,m2=map(int,input().split())
ans=0
for _ in[0]*n:
    h,_,*l=map(int,input().split())
    for i in l:
        ans+=(i*m2>h*k)or(i*m1<h)
print(ans)