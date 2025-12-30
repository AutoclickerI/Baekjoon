def left(n,i,c):
    if 0<=n:
        if s[n][2]!=c:
            left(n-1,-i,s[n][6])
            if i==1:
                s[n]=s[n][-1]+s[n][:-1]
            else:
                s[n]=s[n][1:]+s[n][0]
def right(n,i,c):
    if n<T:
        if s[n][6]!=c:
            right(n+1,-i,s[n][2])
            if i==1:
                s[n]=s[n][-1]+s[n][:-1]
            else:
                s[n]=s[n][1:]+s[n][0]

T=int(input())
s=[input()for _ in[0]*T]
for _ in[0]*int(input()):
    n,i=map(int,input().split())
    n-=1
    left(n-1,-i,s[n][6])
    right(n+1,-i,s[n][2])
    if i==1:
        s[n]=s[n][-1]+s[n][:-1]
    else:
        s[n]=s[n][1:]+s[n][0]
print(sum(int(i[0])for i in s))