for T in range(int(input())):
    N,F=map(eval,input().split())
    s=input()
    m=(1e9,)
    for i in range(N):
        c=0
        for j in range(i,N):
            c+=s[j]=='1'
            m=min((abs(F-c/(j-i+1)),i),m)
    print(f'Case #{T+1}:',m[1])