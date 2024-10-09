a=0
n=int(input())
r=[[]for _ in[0]*100]
for idx,v in enumerate(map(int,input().split())):
    r[v%100]+=idx+1,
    a+=v//100

s=[]
for i in range(100):
    while r[i]:
        for j in range(100-i,100):
            if i==j and len(r[i])<2:
                continue
            if r[j]:
                s+=(r[i].pop(),r[j].pop()),
                a+=1
                break
        else:
            break
print(a)
print(len(s))
for i in s:print(*i)