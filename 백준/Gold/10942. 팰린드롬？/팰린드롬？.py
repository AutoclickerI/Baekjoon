import sys
input=sys.stdin.readline
n=int(input())
l=input().split()
b=[[0]*n for _ in[0]*n]
for i in range(n-1):
    j=1
    while-1<i-j and i+j<len(l)and l[i-j]==l[i+j]:
        b[i-j][i+j]=1
        j+=1
    j=1
    while-2<i-j and i+j<len(l)and l[i-j+1]==l[i+j]:
        b[i-j+1][i+j]=1
        j+=1
for _ in[0]*int(input()):
    p,q=map(int,input().split())
    print(+(p==q)or b[p-1][q-1])