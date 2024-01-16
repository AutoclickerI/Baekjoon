A,B,C=map(int,input().split())
l=[0]*101
for _ in[0]*3:
    for i in range(*map(int,input().split())):
        l[i]+=1
print(sum([0,A,2*B,3*C][i]for i in l))