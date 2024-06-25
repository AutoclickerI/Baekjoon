import sys
input=sys.stdin.readline
input()
s=0
l=s,*[s:=s+i for i in sorted(map(int,input().split()))[::-1]]
from bisect import*
for i in[0]*int(input()):
    print(bisect_left(l,int(input())))