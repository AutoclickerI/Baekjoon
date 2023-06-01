p,q=list(map(int,input().split()))
p=p*q
[print(i-p,end=' ')for i in list(map(int,input().split()))]