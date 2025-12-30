for T in[0]*int(input()):
    input()
    *l,=map(int,input().split())
    M=int(input())+1
    v=[0]*M
    v[0]=1
    for i in l:
        for j in range(i,M):
            v[j]+=v[j-i]
    print(v[-1])