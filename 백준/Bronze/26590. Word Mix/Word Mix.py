p,q=sorted(input().split(),key=len)
for i in range(len(p)):print(end=i%2*q[i]or p[i])