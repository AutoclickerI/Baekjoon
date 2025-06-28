N,M=map(int,input().split())
s=input().split()
t=input().split()
for _ in[0]*int(input()):
    n=int(input())-1
    print(s[n%N]+t[n%M])