D=101
db=[0]*D
db[0]=1
for i in range(100):
    db=[sum(db[max(0,j-1):j+2])for j in range(D)]
cnt=2*10**5//D

print(cnt*D)
sp=-10**6
y=sp

ql=[]

for _ in[0]*cnt:
    for i in range(D):
        print(y,i+sp,+(i<1))
        ql+=(db[i],y,i+sp),
    y+=2
ql.sort()

N=int(input())

ans=[]
while ql and N:
    t,y,x=ql.pop()
    if t<=N:
        N-=t
        ans+=(y,x),
assert N==0 and len(ans)<10000
print(len(ans),100)
for y,x in ans:
    print(y,x)