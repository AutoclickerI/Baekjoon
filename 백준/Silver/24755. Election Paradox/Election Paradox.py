N=int(input())+1
l=sorted(map(int,input().split()))
print(sum([i//2for i in l[:N//2]]+l[N//2:]))