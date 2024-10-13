nums=[[]for _ in range(5*10**6+1)]

for i in range(2,int((5*10**6+1)**.5)+1):
    if nums[i]:
        continue
    for j in range(2*i,5*10**6+1,i):
        nums[j]+=i,

for i in map(int,[*open(0)][1].split()):
    if not nums[i]:
        print(i)
        continue
    l=[]
    for v in nums[i]:
        while i%v<1:
            l+=v,
            i//=v
    if 1<i:
        l+=i,
    print(*l)