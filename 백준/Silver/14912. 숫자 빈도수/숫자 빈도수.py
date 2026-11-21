p,q=input().split()
print(sum(str(~i).count(q)for i in range(int(p))))