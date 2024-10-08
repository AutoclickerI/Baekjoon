for T in range(int(input())):
    s,t=map(int,input().split())
    l=[0]*-~s
    for _ in[0]*t:a,b=map(int,input().split());l[a]+=b
    j=l.index(max(l))
    print(f'Data Set {T+1}:')
    if all(l[j]>2*l[i]for i in range(1,s+1)if i-j):print(f'{j}\n')
    else:print('No suspect.\n')