N=int(input())
l=sorted([input().split()for _ in[0]*6],key=lambda li:56*int(li[4])+24*int(li[3])+14*int(li[2])+6*int(li[1])+30*int(li[5]))[::-1]
ans=0
for i in range(N):
    if l[i%6][0]=='Taiwan':
        ans+=1
print(ans)