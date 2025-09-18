import sys
input=sys.stdin.readline

T=int(input())
while T:
    T-=1
    (_,y),*l=sorted([*map(int,input().split())]for _ in[0]*int(input()))
    a=1
    for _,i in l:
        if i<y:
            a+=1
            y=i
    print(a)