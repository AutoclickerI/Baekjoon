import sys
input=sys.stdin.readline
for _ in[0]*3:
    print([[0,'-'][(l:=(sum(int(input())for _ in[0]*int(input()))))<0],'+'][l>0])