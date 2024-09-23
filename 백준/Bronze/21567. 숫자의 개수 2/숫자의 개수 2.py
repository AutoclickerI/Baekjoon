A,B,C=map(int,open(0))
print(*map(str(A*B*C).count,map(str,range(10))))