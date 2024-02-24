N,S=map(int,input().split())
b=[0]*4000001
for i in map(int,input().split()):
    tmp=[0]*4000001
    tmp[i]+=1
    for j in range(-2000000,2000001):
        if abs(i+j)>2000000:
            continue
        tmp[i+j]+=b[j]+b[i+j]
    b=tmp
print(b[S])