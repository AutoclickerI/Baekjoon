N=int(input())
S=sorted
print(S(eval('S(map(int,input().split()))[N//2],'*N))[N//2])