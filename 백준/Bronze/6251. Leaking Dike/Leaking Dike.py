while n:=int(input()):
    *l,=map(int,input().split())
    n=l[int(input())-1]+1
    print(sum(max(n-i,0)for i in l))