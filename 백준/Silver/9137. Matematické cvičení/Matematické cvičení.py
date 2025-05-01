import sys

sys.setrecursionlimit(10**6)

def to_n(v,b):
    if v==0:return''
    if b==1:
        return'1'*v
    else:
        return to_n(v//b,b)+'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[v%b]

def to_10(v,b):
    n=0
    for i in v:
        n*=b
        n+='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(i)
    return n

while n:=int(input()):
    a,b=input().split()
    if n==1:
        v=len((a+b).strip('0'))
    else:
        v=to_10(a,n)+to_10(b,n)
    print(a,'+',b,'=',to_n(v,n)or 0)