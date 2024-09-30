N=int(input())
l=[f'{i:b}'.zfill(N)for i in range(2**N)]
l.sort(key=lambda s:(s.count('1'),s[::-1]))
print(l.index(input()))