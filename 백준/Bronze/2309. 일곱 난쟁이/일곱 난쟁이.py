l=[int(input())for i in[0]*9]
p=sum(l)-100
try:
    for i in range(9):
        for j in range(i+1,9):
            if l[i]+l[j]==p:
                raise
except:
    del l[j]
    del l[i]
    print(*sorted(l))