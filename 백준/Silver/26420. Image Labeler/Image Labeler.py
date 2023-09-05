for i in range(int(input())):
    n,m=map(int,input().split())
    l=sorted(map(int,input().split()))+[0]
    n-=m
    print(f'Case #{i+1}:',sum(l[-m:])+(l[n//2]+l[-~n//2])/2)