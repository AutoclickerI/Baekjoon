p=range(int(input()))
l=[*map(int,input().split())]
print(sum(p[i]+1!=l[i]for i in range(len(l))))