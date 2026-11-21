from bisect import*
input()
l=sorted(map(int,input().split()))+[2**31]
input()
for i in[*map(int,input().split())]:print(+(i==l[bisect_left(l,i)]))