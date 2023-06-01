from bisect import*
input()
l=sorted(map(int,input().split()))+[2**31]
input()
p=[*map(int,input().split())]
for i in p:
    print(+(i==l[bisect_left(l,i)]))