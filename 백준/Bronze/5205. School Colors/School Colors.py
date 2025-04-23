for T in range(int(input())):
    print(f'Data Set {T+1}:')
    n=int(input())
    l=[[*map(int,input().split())]for _ in[0]*n]
    mv=max(sum((j-i)**2for i,j in zip(l[i],l[j]))for i in range(n)for j in range(n))
    for i in range(n):
        for j in range(i,n):
            sum((j-i)**2for i,j in zip(l[i],l[j]))==mv!=print(i+1,j+1)