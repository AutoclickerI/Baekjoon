for k in range(int(input())):
    m=a=0
    for i,j in sorted([[*map(int,input().split())]for _ in[0]*int(input())]):
        a+=j<m
        m=max(m,j)
    print(f'Case #{k+1}:',a)