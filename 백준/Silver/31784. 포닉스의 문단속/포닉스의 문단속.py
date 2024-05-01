N,K=map(int,input().split())
*s,=input()
for i in range(N):
    if 25>90-ord(s[i])<K:
        K-=91-ord(s[i])
        s[i]='A'
s[-1]=chr(ord(s[-1])+K%26)
print(*s,sep='')