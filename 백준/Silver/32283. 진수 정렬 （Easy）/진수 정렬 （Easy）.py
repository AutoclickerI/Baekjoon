N=int(input())
print(sorted([f'{i:b}'.zfill(N)for i in range(2**N)],key=lambda s:(s.count('1'),s[::-1])).index(input()))