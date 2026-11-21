import sys
input=sys.stdin.readline
h,m,s=map(int,input().split())
t=(h*60+m)*60+s
for _ in[0]*int(input()):
    *p,=map(int,input().split())
    if len(p)-1:
        t-=(p[0]*2-3)*p[1]
        t%=86400
    else:
        print(t//3600,t//60%60,t%60)