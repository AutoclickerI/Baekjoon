v=[0]*100001
v[0]=1
v[1]=1
v[2]=2
v[3]=2
for i in range(4,100001):
    v[i]=v[i-2]+v[i-4]+v[i-6]
for i in[*open(0)][1:]:
    print(v[int(i)]%(10**9+9))