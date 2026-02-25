def p(s):
    return int(s[:2])*3600+int(s[3:5])*60+int(s[6:])

n,m=map(int,input().split())
s=[p(input())for _ in[0]*n]
e=[p(input())for _ in[0]*m]
v=int(input())

print(min([j-i for i in s for j in e if v<=j-i]or[-1]))