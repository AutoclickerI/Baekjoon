c=0
H,M=map(int,input().split())
for i in range(H):
    for j in range(M):
        s=str(i)+str(j)
        v='0'
        for x in s.replace('0',''):
            if x!=v[-1]:v+=x
        if'239'in v:c+=1
print(c)