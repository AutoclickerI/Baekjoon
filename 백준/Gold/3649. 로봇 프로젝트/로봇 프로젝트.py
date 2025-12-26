import sys
input=sys.stdin.readline
while x:=input():
    x=int(x)*10000000
    n=int(input())
    l=sorted(int(input())for _ in[0]*n)
    s=0
    e=n-1
    while s<e:
        if l[s]+l[e]==x:
            print('yes',l[s],l[e])
            break
        if l[s]+l[e]<x:
            s+=1
        else:
            e-=1
    else:
        print('danger')