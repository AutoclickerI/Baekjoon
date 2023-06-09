import sys
input=sys.stdin.readline
for _ in[0]*int(input()):p,q=map(int,input().split());l=[int(input())for _ in[0]*q];print(max(min(i,p-i)for i in l),max(max(i,p-i)for i in l))