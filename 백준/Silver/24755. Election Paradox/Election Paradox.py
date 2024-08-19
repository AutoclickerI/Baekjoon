N=int(input())+1
l=sorted(map(int,input().split()))
print(sum(l)+sum(~i//2for i in l[:N//2]))