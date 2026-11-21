x=sum(a:=[*map(int,input().split())])+1
print(min(x//2+1,x-max(a)))