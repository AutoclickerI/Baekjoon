for _ in[0]*int(input()):
    input()
    *l,=map(int,input().split())
    M=int(input())
    v=[0]*-~M
    v[0]=1
    for i in l:
        for j in range(M+1):
            if 0<=j-i:
                v[j]+=v[j-i]
    print(v[-1])