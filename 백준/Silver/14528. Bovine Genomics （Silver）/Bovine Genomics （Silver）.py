N,M=map(int,input().split())
spotty=eval('input(),'*N)
plain=eval('input(),'*N)
ans=0
for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            s=set()
            for x in spotty:
                s.add(x[i]+x[j]+x[k])
            for x in plain:
                if x[i]+x[j]+x[k]in s:
                    break
            else:
                ans+=1
print(ans)