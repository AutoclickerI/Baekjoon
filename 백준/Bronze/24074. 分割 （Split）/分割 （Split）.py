input()
b=list(map(int,input().split()))
c=b.index(sorted(b)[-1])
print(sum(b[:c]),sum(b[c+1:]))