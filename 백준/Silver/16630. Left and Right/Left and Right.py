input()
i=1
for l in input().split('R'):print(*range(i,i:=i-~len(l))[::-1])