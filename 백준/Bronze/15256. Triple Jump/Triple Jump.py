for T in range(int(input())):
    n=int(input())
    *l,=map(eval,input().split())
    s=n
    for i in range(n):
        if 30<=l[i]<=30.2:s=i;break
    print(f'Data Set {T+1}:\n{s<n-3and min(l[s+3:])-30:.2f}\n')