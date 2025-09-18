def left(n,i,c):
    if 0<=n:
        if s[n][2]!=c:
            left(n-1,-i,s[n][6])
            if i==1:
                s[n]=s[n][-1]+s[n][:-1]
            else:
                s[n]=s[n][1:]+s[n][0]
def right(n,i,c):
    if n<4:
        if s[n][6]!=c:
            right(n+1,-i,s[n][2])
            if i==1:
                s[n]=s[n][-1]+s[n][:-1]
            else:
                s[n]=s[n][1:]+s[n][0]
s=[input()for _ in[0]*4]
for _ in[0]*int(input()):
    n,i=map(int,input().split())
    n-=1
    left(n-1,-i,s[n][6])
    right(n+1,-i,s[n][2])
    if i==1:
        s[n]=s[n][-1]+s[n][:-1]
    else:
        s[n]=s[n][1:]+s[n][0]
print(int(s[0][0])+int(s[1][0])*2+int(s[2][0])*4+int(s[3][0])*8)