p,q=open(0)
print(sum(abs(p.count(i)-q.count(i))for i in'RGBY')//2)