import sys

sys.setrecursionlimit(10**6)

def to_n(v,b):
    if v==0:return''
    if b==1:
        return'1'*v
    else:
        return to_n(v//b,b)+'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[v%b]

while n:=int(input()):
    a,b=input().split()
    if n==1:
        v=len((a+b).strip('0'))
    else:
        v=int(a,n)+int(b,n)
    print(a,'+',b,'=',to_n(v,n)or 0)