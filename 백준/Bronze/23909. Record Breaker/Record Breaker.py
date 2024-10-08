for T in range(int(input())):
    n=int(input())
    m=-1
    l=-1,*map(int,input().split()),-1
    a=0
    for i in range(1,n+1):
        if l[i]>m:
            m=l[i]
            a+=l[i]>l[i+1]
    print(f'Case #{T+1}:',a)