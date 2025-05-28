N,M,K,s=open(0).read().split()
l=[0]*8
l[int(N)*2+int(M)-3]=1
A,B,C,D,E,F,G,H=l
for i in s:
    if i=='A':
        A,B,C,D,E,F,G,H=E,F,G,H,A,B,C,D
    if i=='B':
        A,B,C,D,E,F,G,H=D,C,B,A,H,G,F,E
    if i=='C':
        A,B,C,D,E,F,G,H=H,G,F,E,D,C,B,A
    if i=='D':
        A,B,C,D,E,F,G,H=C,A,E,B,G,D,H,F
idx=[A,B,C,D,E,F,G,H].index(1)
print(idx//2+1,idx%2+1)