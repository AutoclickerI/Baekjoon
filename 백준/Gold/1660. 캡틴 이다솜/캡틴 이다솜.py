l=[i*~i*~-~i//6 for i in range(123)][1:]
v=[0]+[float('inf')]*300000

for i in range(1,300001):
    for j in l:
        if j<=i:
            v[i]=min(v[i],v[i-j]+1)
print(v[int(input())])