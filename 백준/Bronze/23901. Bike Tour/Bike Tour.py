for i in range(int(input())):
    n=int(input())
    *l,=map(int,input().split())
    print(f'Case #{i+1}:',sum(l[i-1]<l[i]>l[i+1]for i in range(1,n-1)))