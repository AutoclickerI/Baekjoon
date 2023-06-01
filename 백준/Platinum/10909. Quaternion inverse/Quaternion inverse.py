import sys
input=sys.stdin.readline
p,q=map(int,input().split())
for i in[0]*q:
    a,b,c,d=map(int,input().split())
    A=a*a+b*b+c*c+d*d
    try:
        H=pow(A,-1,p)
        print(*(i*H for i in[a,-b,-c,-d]))
    except:
        print(0,0,0,0)