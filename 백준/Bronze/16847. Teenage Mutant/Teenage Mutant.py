for i in range(int(input())):
    n,k=map(int,input().split())
    m=input()
    l=[input()for _ in[0]*n]
    a=0
    for j in range(k):a+=all(m[j]!=o[j]for o in l)
    print(f'Data Set {i+1}:\n{a}/{k}\n')