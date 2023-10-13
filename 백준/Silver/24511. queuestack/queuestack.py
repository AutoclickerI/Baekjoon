input()
l=[j for i,j in zip(input().split(),map(int,input().split()))if'1'>i][::-1]
n=int(input())
l+=map(int,input().split())
print(*l[:n])