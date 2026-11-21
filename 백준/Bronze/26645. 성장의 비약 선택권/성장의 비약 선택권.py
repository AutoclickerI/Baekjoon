n=int(input())
l=[min(240,n+1),min(230,n+2),min(220,n+4),min(210,n+8)]
print(4-l.index(max(l)))